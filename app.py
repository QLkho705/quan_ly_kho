from flask import Flask, render_template, request, redirect, url_for, session, send_file
import sqlite3
import io
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = "secret705"  # khóa session

# =========================
# TẠO DATABASE LẦN ĐẦU
# =========================
def init_db():
    conn = sqlite3.connect("kho.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS lichsu(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doi TEXT,
                tenhang TEXT,
                soluong INTEGER,
                loaigd TEXT,
                ngay TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    # Tạo admin mặc định
    c.execute("INSERT OR IGNORE INTO users(username, password) VALUES (?, ?)", ("admin", "admin"))
    conn.commit()
    conn.close()

init_db()

# =========================
# ROUTES
# =========================
@app.route("/")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

# ---- LOGIN ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        conn = sqlite3.connect("kho.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
        user = c.fetchone()
        conn.close()
        if user:
            session["username"] = u
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ---- NHẬP ----
@app.route("/nhap", methods=["GET", "POST"])
def nhap():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        doi = request.form["doi"]
        tenhang = request.form["tenhang"]
        soluong = int(request.form["soluong"])
        conn = sqlite3.connect("kho.db")
        c = conn.cursor()
        c.execute("INSERT INTO lichsu(doi, tenhang, soluong, loaigd) VALUES (?, ?, ?, ?)",
                  (doi, tenhang, soluong, "Nhập"))
        conn.commit()
        conn.close()
        return redirect(url_for("lichsu"))
    return render_template("nhap.html")

# ---- XUẤT ----
@app.route("/xuat", methods=["GET", "POST"])
def xuat():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        doi = request.form["doi"]
        tenhang = request.form["tenhang"]
        soluong = int(request.form["soluong"])
        conn = sqlite3.connect("kho.db")
        c = conn.cursor()
        c.execute("INSERT INTO lichsu(doi, tenhang, soluong, loaigd) VALUES (?, ?, ?, ?)",
                  (doi, tenhang, soluong, "Xuất"))
        conn.commit()
        conn.close()
        return redirect(url_for("lichsu"))
    return render_template("xuat.html")

# ---- LỊCH SỬ ----
@app.route("/lichsu")
def lichsu():
    if "username" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect("kho.db")
    c = conn.cursor()
    c.execute("SELECT doi, tenhang, soluong, loaigd, ngay FROM lichsu ORDER BY ngay DESC")
    data = c.fetchall()
    conn.close()
    return render_template("lichsu.html", data=data)

# ---- BÁO CÁO ----
@app.route("/baocao")
def baocao():
    if "username" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect("kho.db")
    c = conn.cursor()
    c.execute("""
        SELECT doi, tenhang,
               SUM(CASE WHEN loaigd='Nhập' THEN soluong ELSE -soluong END) as tonkho
        FROM lichsu GROUP BY doi, tenhang
    """)
    data = c.fetchall()
    conn.close()
    return render_template("baocao.html", data=data)

# ---- XUẤT EXCEL ----
@app.route("/baocao/excel")
def export_excel():
    conn = sqlite3.connect("kho.db")
    df = pd.read_sql_query("""
        SELECT doi, tenhang,
               SUM(CASE WHEN loaigd='Nhập' THEN soluong ELSE -soluong END) as tonkho
        FROM lichsu GROUP BY doi, tenhang
    """, conn)
    conn.close()
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="BaoCaoTonKho")
    output.seek(0)
    return send_file(output, as_attachment=True,
                     download_name="BaoCaoTonKho.xlsx",
                     mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# ---- XUẤT PDF ----
@app.route("/baocao/pdf")
def export_pdf():
    conn = sqlite3.connect("kho.db")
    c = conn.cursor()
    c.execute("""
        SELECT doi, tenhang,
               SUM(CASE WHEN loaigd='Nhập' THEN soluong ELSE -soluong END) as tonkho
        FROM lichsu GROUP BY doi, tenhang
    """)
    data = c.fetchall()
    conn.close()

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    elements.append(Paragraph("BÁO CÁO TỒN KHO - KHO 705", styles["Title"]))

    table_data = [["Đội", "Tên hàng", "Số lượng tồn"]] + list(data)
    table = Table(table_data, colWidths=[100, 200, 100])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.green),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ]))
    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    return send_file(buffer, as_attachment=True,
                     download_name="BaoCaoTonKho.pdf",
                     mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)