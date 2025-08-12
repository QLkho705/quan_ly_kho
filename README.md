# quan_ly_kho
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Kho 705 - Full (Admin/Thủ kho)</title>
<!-- Styles -->
<style>
  :root{--green:#0b7a3a;--light:#f6fff6;--card:#fff;}
  body{font-family:Arial,Helvetica,sans-serif;background:var(--light);margin:0;padding:12px;color:#083;}
  h1,h2{margin:6px 0;color:var(--green)}
  .card{background:var(--card);padding:12px;border-radius:8px;box-shadow:0 1px 6px rgba(0,0,0,0.06);margin-bottom:12px}
  input,select,button,textarea{padding:8px;margin:6px 0;border:1px solid #ddd;border-radius:6px;width:100%;box-sizing:border-box}
  .row{display:flex;gap:10px}
  .col{flex:1}
  table{width:100%;border-collapse:collapse;font-size:13px}
  th,td{border:1px solid #e6e6e6;padding:6px;text-align:center}
  th{background:#eafaf0}
  .hidden{display:none}
  .small{font-size:13px;color:#555}
  .topbar{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px}
  .btn-inline{display:inline-block;padding:6px 10px;margin:2px;border-radius:6px;background:var(--green);color:white;border:none}
  .danger{background:#c0392b}
  @media(max-width:720px){.row{flex-direction:column}}
</style>
</head>
<body>

<!-- LOGIN -->
<div id="loginCard" class="card">
  <h1>🔐 Đăng nhập - Kho 705</h1>
  <input id="username" placeholder="Tên đăng nhập" value="">
  <input id="password" type="password" placeholder="Mật khẩu" value="">
  <button onclick="login()">Đăng nhập</button>
  <p class="small">Tài khoản mặc định: <b>admin / 123456</b> (Admin), <b>thukho / 123456</b> (Thủ kho - Đội 2). Admin có quyền tạo tài khoản.</p>
</div>

<!-- APP -->
<div id="app" class="hidden">

  <div class="topbar">
    <div style="display:flex;gap:8px;align-items:center">
      <h1 style="margin:0">📦 Kho 705</h1>
      <div id="userLabel" class="small"></div>
    </div>
    <div style="display:flex;gap:6px">
      <button onclick="showChangePassword()" class="btn-inline">🔒 Đổi mật khẩu</button>
      <button onclick="logout()" class="btn-inline">🚪 Đăng xuất</button>
    </div>
  </div>

  <!-- CHANGE PASS -->
  <div id="changePass" class="card hidden">
    <h3>Đổi mật khẩu</h3>
    <input id="oldPass" type="password" placeholder="Mật khẩu cũ">
    <input id="newPass" type="password" placeholder="Mật khẩu mới">
    <button onclick="changePassword()">Lưu mật khẩu mới</button>
  </div>

  <!-- USER MANAGEMENT (Admin) -->
  <div id="userMng" class="card hidden">
    <h3>Quản lý người dùng (Admin)</h3>
    <div style="display:flex;gap:8px">
      <input id="newUser" placeholder="Tên đăng nhập (ví dụ: thukho2)">
      <input id="newPassw" placeholder="Mật khẩu">
      <select id="newRole">
        <option value="thukho">Thủ kho</option>
        <option value="admin">Admin</option>
      </select>
    </div>
    <div style="display:flex;gap:8px">
      <select id="newTeam">
        <option value="">(chọn đội cho Thủ kho)</option>
        <option>Đội 2</option>
        <option>Đội 4</option>
        <option>Đội 7</option>
        <option>Đội 10</option>
        <option>Ngoài</option>
      </select>
      <button onclick="createUser()" class="btn-inline">Tạo người dùng</button>
    </div>

    <h4 style="margin-top:10px">Danh sách người dùng</h4>
    <table>
      <thead><tr><th>Tên</th><th>Quyền</th><th>Đội</th><th>Hành động</th></tr></thead>
      <tbody id="usersTable"></tbody>
    </table>
  </div>

  <!-- INPUT / OUTPUT -->
  <div class="card">
    <h3>Nhập hàng (tổng)</h3>
    <div class="row">
      <div class="col"><input id="tenNhap" placeholder="Tên hàng (ví dụ: NPK 16-16-8)"></div>
      <div class="col"><input id="slNhap" type="number" placeholder="Số lượng"></div>
      <div class="col">
        <select id="cateNhap">
          <option value="Phân bón">Phân bón</option>
          <option value="Vật tư">Vật tư</option>
          <option value="Thuốc BVTV">Thuốc BVTV</option>
          <option value="Cà phê">Cà phê</option>
        </select>
      </div>
    </div>
    <button onclick="nhapKho()">➕ Nhập kho</button>
  </div>

  <div class="card">
    <h3>Xuất hàng theo đội</h3>
    <div class="row">
      <div class="col"><input id="tenXuat" placeholder="Tên hàng"></div>
      <div class="col"><input id="slXuat" type="number" placeholder="Số lượng"></div>
      <div class="col">
        <select id="doiXuat">
          <option>Đội 2</option>
          <option>Đội 4</option>
          <option>Đội 7</option>
          <option>Đội 10</option>
          <option>Ngoài</option>
        </select>
      </div>
    </div>
    <button onclick="xuatKho()">📤 Xuất kho</button>
  </div>

  <!-- STOCK -->
  <div class="card">
    <h3>Tồn kho</h3>
    <table>
      <thead><tr><th>Tên hàng</th><th>Danh mục</th><th>Số lượng</th></tr></thead>
      <tbody id="bangKho"></tbody>
    </table>
  </div>

  <!-- FILTER / REPORT -->
  <div class="card">
    <h3>Báo cáo & Lọc lịch sử</h3>
    <div class="row">
      <div class="col"><input id="fromDate" type="date"></div>
      <div class="col"><input id="toDate" type="date"></div>
      <div class="col">
        <select id="filterTeam">
          <option value="all">Tất cả đội</option>
          <option>Đội 2</option>
          <option>Đội 4</option>
          <option>Đội 7</option>
          <option>Đội 10</option>
          <option>Ngoài</option>
        </select>
      </div>
    </div>
    <div class="row">
      <div class="col"><input id="filterItem" placeholder="Tên hàng (lọc, để trống = tất cả)"></div>
      <div class="col">
        <select id="filterType">
          <option value="all">Tất cả</option>
          <option value="Nhập">Nhập</option>
          <option value="Xuất">Xuất</option>
        </select>
      </div>
      <div class="col">
        <button onclick="applyFilter()" class="btn-inline">Áp dụng lọc</button>
        <button onclick="resetFilter()" class="btn-inline">Reset</button>
      </div>
    </div>

    <h4 style="margin-top:8px">Lịch sử (kết quả lọc)</h4>
    <table>
      <thead><tr><th>Thời gian</th><th>Loại</th><th>Tên</th><th>SL</th><th>Đội</th><th>Danh mục</th></tr></thead>
      <tbody id="bangLichSu"></tbody>
    </table>

    <div style="display:flex;gap:8px;margin-top:8px">
      <button onclick="exportPDFFiltered()" class="btn-inline">📄 Xuất PDF (đang lọc)</button>
      <button onclick="exportExcelFiltered()" class="btn-inline">📊 Xuất Excel (đang lọc)</button>
      <button onclick="sendReportEmail()" class="btn-inline">✉️ Gửi mail (cần backend)</button>
      <button onclick="saveToDrive()" class="btn-inline">📁 Lưu Drive (cần backend)</button>
    </div>
  </div>

  <!-- CHARTS -->
  <div class="card">
    <h3>Biểu đồ</h3>
    <div class="row">
      <div class="col">
        <h4 style="margin:6px 0">Tồn kho theo danh mục</h4>
        <canvas id="stockChart" height="220"></canvas>
      </div>
      <div class="col">
        <h4 style="margin:6px 0">Xuất theo đội</h4>
        <canvas id="exportChart" height="220"></canvas>
      </div>
    </div>
  </div>

  <div style="text-align:center" class="small">Dữ liệu được lưu trong trình duyệt (localStorage). Muốn đồng bộ lên Google Drive / gửi mail, cài backend theo hướng dẫn mình sẽ gửi.</div>
</div>

<!-- libs -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>

<!-- App JS -->
<script>
/*
  Kho 705 - Single-file app
  Data in localStorage:
    - users705: [{user, pass, role('admin'|'thukho'), team}]
    - kho705: [{ten,cate,sl}]
    - lichSu705: [{timeISO,loai,ten,sl,doi,cate,user}]
*/

const LS_USERS = "users705";
const LS_KHO = "kho705";
const LS_LS = "lichSu705";

let users = JSON.parse(localStorage.getItem(LS_USERS) || "null");
let kho = JSON.parse(localStorage.getItem(LS_KHO) || "null");
let lichSu = JSON.parse(localStorage.getItem(LS_LS) || "null");

if (!users) {
  users = [
    {user:"admin", pass:"123456", role:"admin", team:""},
    {user:"thukho", pass:"123456", role:"thukho", team:"Đội 2"}
  ];
  localStorage.setItem(LS_USERS, JSON.stringify(users));
}
if (!kho) { kho = []; localStorage.setItem(LS_KHO, JSON.stringify(kho)); }
if (!lichSu) { lichSu = []; localStorage.setItem(LS_LS, JSON.stringify(lichSu)); }

let currentUser = null;
let currentFiltered = []; // history filtered
let stockChart=null, exportChart=null;

/* ----------------- Auth ----------------- */
function login(){
  const u = document.getElementById("username").value.trim();
  const p = document.getElementById("password").value.trim();
  const found = users.find(x=>x.user===u && x.pass===p);
  if (!found) return alert("Sai tài khoản hoặc mật khẩu");
  currentUser = found;
  document.getElementById("loginCard").classList.add("hidden");
  document.getElementById("app").classList.remove("hidden");
  document.getElementById("userLabel").innerText = `${currentUser.user} (${currentUser.role}${currentUser.team? ' - ' + currentUser.team : ''})`;
  // show admin panel if admin
  document.getElementById("userMng").classList.toggle("hidden", currentUser.role!=="admin");
  renderAll();
}
function logout(){
  currentUser=null;
  document.getElementById("app").classList.add("hidden");
  document.getElementById("loginCard").classList.remove("hidden");
  document.getElementById("username").value="";
  document.getElementById("password").value="";
}
function showChangePassword(){ document.getElementById("changePass").classList.toggle("hidden"); }
function changePassword(){
  const oldP = document.getElementById("oldPass").value.trim();
  const newP = document.getElementById("newPass").value.trim();
  if (!currentUser) return alert("Bạn phải đăng nhập");
  if (oldP !== currentUser.pass) return alert("Mật khẩu cũ không đúng");
  if (!newP) return alert("Mật khẩu mới không hợp lệ");
  // update user list
  users = users.map(u => u.user===currentUser.user ? {...u, pass:newP} : u);
  localStorage.setItem(LS_USERS, JSON.stringify(users));
  currentUser.pass = newP;
  alert("Đổi mật khẩu thành công");
  document.getElementById("oldPass").value=""; document.getElementById("newPass").value="";
  document.getElementById("changePass").classList.add("hidden");
}

/* -------------- User management (Admin) -------------- */
function renderUsers(){
  const tbody = document.getElementById("usersTable");
  tbody.innerHTML = users.map(u => `
    <tr>
      <td>${u.user}</td>
      <td>${u.role}</td>
      <td>${u.team||""}</td>
      <td>
        <button onclick="promptEditUser('${u.user}')">Sửa</button>
        <button onclick="deleteUser('${u.user}')" class="danger">Xóa</button>
      </td>
    </tr>
  `).join("");
}
function createUser(){
  const name = document.getElementById("newUser").value.trim();
  const passw = document.getElementById("newPassw").value.trim();
  const role = document.getElementById("newRole").value;
  const team = document.getElementById("newTeam").value;
  if (!name || !passw) return alert("Nhập tên và mật khẩu");
  if (users.find(u=>u.user===name)) return alert("Người dùng đã tồn tại");
  users.push({user:name, pass:passw, role:role, team: role==="thukho" ? team : ""});
  localStorage.setItem(LS_USERS, JSON.stringify(users));
  document.getElementById("newUser").value=""; document.getElementById("newPassw").value="";
  renderUsers();
  alert("Tạo user thành công");
}
function promptEditUser(username){
  const u = users.find(x=>x.user===username);
  if (!u) return;
  const newPass = prompt("Mật khẩu mới (để trống giữ nguyên):", "");
  const newRole = prompt("Quyền (admin / thukho):", u.role);
  const newTeam = prompt("Đội (nếu thukho):", u.team||"");
  if (newPass) u.pass = newPass;
  if (newRole) u.role = newRole;
  u.team = newRole==="thukho" ? newTeam : "";
  users = users.map(x=>x.user===u.user?u:x);
  localStorage.setItem(LS_USERS, JSON.stringify(users));
  renderUsers();
  alert("Cập nhật user xong");
}
function deleteUser(username){
  if (!confirm("Xác nhận xóa user " + username + "?")) return;
  users = users.filter(u=>u.user!==username);
  localStorage.setItem(LS_USERS, JSON.stringify(users));
  renderUsers();
}

/* ----------------- Kho / Lịch sử ----------------- */
function saveAll(){
  localStorage.setItem(LS_KHO, JSON.stringify(kho));
  localStorage.setItem(LS_LS, JSON.stringify(lichSu));
  renderAll();
}
function renderKho(){
  const tbody = document.getElementById("bangKho");
  tbody.innerHTML = kho.map(i=>`<tr><td>${i.ten}</td><td>${i.cate||""}</td><td>${i.sl}</td></tr>`).join("");
}
function renderHistory(list){
  const tbody = document.getElementById("bangLichSu");
  tbody.innerHTML = list.map(h=>{
    const t = new Date(h.timeISO).toLocaleString();
    return `<tr><td>${t}</td><td>${h.loai}</td><td>${h.ten}</td><td>${h.sl}</td><td>${h.doi||""}</td><td>${h.cate||""}</td></tr>`;
  }).join("");
}

function nhapKho(){
  if (!currentUser) return alert("Đăng nhập để thao tác");
  const ten = document.getElementById("tenNhap").value.trim();
  const sl = parseInt(document.getElementById("slNhap").value);
  const cate = document.getElementById("cateNhap").value;
  if (!ten || isNaN(sl) || sl<=0) return alert("Nhập tên + số lượng (>0)");
  let item = kho.find(x=>x.ten===ten);
  if (item) item.sl += sl; else kho.push({ten,cate,sl});
  lichSu.push({timeISO:(new Date()).toISOString(), loai:"Nhập", ten, sl, doi:"", cate, user:currentUser.user});
  saveAll();
  document.getElementById("tenNhap").value=""; document.getElementById("slNhap").value="";
  updateCharts();
}

function xuatKho(){
  if (!currentUser) return alert("Đăng nhập để thao tác");
  // Thủ kho chỉ được xuất cho đội của mình (nếu role thukho)
  const ten = document.getElementById("tenXuat").value.trim();
  const sl = parseInt(document.getElementById("slXuat").value);
  const doi = document.getElementById("doiXuat").value;
  if (!ten || isNaN(sl) || sl<=0) return alert("Nhập tên + số lượng (>0)");
  // role check
  if (currentUser.role==="thukho" && currentUser.team && currentUser.team !== doi) {
    return alert("Bạn chỉ được xuất cho đội bạn được gán ("+currentUser.team+")");
  }
  let item = kho.find(x=>x.ten===ten);
  if (!item || item.sl < sl) return alert("Không đủ hàng trong kho");
  item.sl -= sl;
  if (item.sl <= 0) kho = kho.filter(x=>x.ten!==ten);
  lichSu.push({timeISO:(new Date()).toISOString(), loai:"Xuất", ten, sl, doi, cate:item.cate||"", user:currentUser.user});
  saveAll();
  document.getElementById("tenXuat").value=""; document.getElementById("slXuat").value="";
  updateCharts();
}

/* ------------- Filter / Export -------------- */
function applyFilter(){
  const from = document.getElementById("fromDate").value;
  const to = document.getElementById("toDate").value;
  const team = document.getElementById("filterTeam").value;
  const item = document.getElementById("filterItem").value.trim().toLowerCase();
  const type = document.getElementById("filterType").value;
  let list = [...lichSu];
  if (from) {
    const f = new Date(from+"T00:00:00");
    list = list.filter(x=> new Date(x.timeISO) >= f);
  }
  if (to) {
    const t = new Date(to+"T23:59:59");
    list = list.filter(x=> new Date(x.timeISO) <= t);
  }
  if (team!=="all") list = list.filter(x=> x.doi===team);
  if (item) list = list.filter(x=> (x.ten||"").toLowerCase().includes(item));
  if (type!=="all") list = list.filter(x=> x.loai===type);
  // if currentUser is thukho, only show their team's records
  if (currentUser.role==="thukho" && currentUser.team) {
    list = list.filter(x=> x.doi===currentUser.team || x.loai==="Nhập"); // allow imports to be seen
  }
  list.sort((a,b)=> new Date(b.timeISO)-new Date(a.timeISO));
  currentFiltered = list;
  renderHistory(list);
}
function resetFilter(){
  document.getElementById("fromDate").value=""; document.getElementById("toDate").value="";
  document.getElementById("filterTeam").value="all"; document.getElementById("filterItem").value=""; document.getElementById("filterType").value="all";
  applyFilter();
}

/* ---------- Export PDF / Excel ---------- */
// small embedded logo (SVG -> base64)
const logoBase64 = 'data:image/svg+xml;base64,' + btoa(`<svg xmlns='http://www.w3.org/2000/svg' width='200' height='60'><rect rx='8' ry='8' width='200' height='60' fill='#0b7a3a'/><text x='50%' y='57%' font-family='Arial' font-size='28' fill='white' text-anchor='middle' dominant-baseline='middle'>705</text></svg>`);

function exportPDFFiltered(){
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF({unit:'pt',format:'a4'});
  doc.setFontSize(16);
  // add logo
  doc.addImage(logoBase64, 'PNG', 40, 30, 80, 30);
  doc.text('Báo cáo Kho 705', 140, 50);
  doc.setFontSize(10);
  let y = 90;
  const rows = currentFiltered.slice(0, 500); // cap
  rows.forEach(r=>{
    const t = new Date(r.timeISO).toLocaleString();
    const line = `${t} | ${r.loai} | ${r.ten} | ${r.sl} | ${r.doi||''} | ${r.cate||''} | ${r.user||''}`;
    doc.text(line, 40, y);
    y += 12;
    if (y > 750) { doc.addPage(); y = 40; }
  });
  doc.save('bao_cao_kho705.pdf');
}

function exportExcelFiltered(){
  const data = currentFiltered.map(r=>({
    ThoiGian: new Date(r.timeISO).toLocaleString(),
    Loai: r.loai,
    Ten: r.ten,
    SoLuong: r.sl,
    Doi: r.doi||"",
    DanhMuc: r.cate||"",
    Nguoi: r.user||""
  }));
  const ws = XLSX.utils.json_to_sheet(data);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "LichSu");
  XLSX.writeFile(wb, "bao_cao_kho705.xlsx");
}

/* --------- Email / Google Drive (placeholders) ---------- */
/*
  NOTE: To actually send email or save to Google Drive you'll need a backend service.
  The functions below show how to POST the generated file to a backend endpoint:
  - /upload-drive  (accepts form-data: file)
  - /send-report  (accepts form-data: file, to_email)

  I'll provide a Flask backend example if you want. For now these functions will
  create the PDF/Excel file in browser and then attempt to POST to the configured endpoint.
*/

async function sendReportEmail(){
  // create PDF blob
  const pdfBlob = await generatePdfBlob();
  const to = prompt("Gửi tới email (ví dụ: you@example.com):","");
  if (!to) return;
  // POST to backend
  const endpoint = prompt("Nhập endpoint backend gửi mail (ví dụ: https://example.com/send-report):","");
  if (!endpoint) {
    alert("Bạn chưa cung cấp endpoint backend. Mình sẽ lưu file PDF xuống máy.");
    downloadBlob(pdfBlob, "bao_cao_kho705.pdf");
    return;
  }
  const fd = new FormData();
  fd.append('file', pdfBlob, 'bao_cao_kho705.pdf');
  fd.append('to', to);
  try {
    const resp = await fetch(endpoint, {method:'POST', body:fd});
    if (resp.ok) alert("Yêu cầu gửi mail đã được gửi tới backend.");
    else alert("Backend trả lỗi: " + resp.statusText);
  } catch(e){ alert("Lỗi gửi tới backend: " + e.message); }
}

async function saveToDrive(){
  const pdfBlob = await generatePdfBlob();
  const endpoint = prompt("Nhập endpoint backend upload Drive (ví dụ: https://example.com/upload-drive):","");
  if (!endpoint) {
    alert("Bạn chưa cung cấp endpoint backend. Mình sẽ lưu file PDF xuống máy.");
    downloadBlob(pdfBlob, "bao_cao_kho705.pdf");
    return;
  }
  const fd = new FormData();
  fd.append('file', pdfBlob, 'bao_cao_kho705.pdf');
  try {
    const resp = await fetch(endpoint, {method:'POST', body:fd});
    if (resp.ok) {
      const json = await resp.json();
      alert("Upload xong. Link (backend trả về): " + (json.link||"không có"));
    } else alert("Backend trả lỗi: " + resp.statusText);
  } catch(e){ alert("Lỗi upload tới backend: " + e.message); }
}

function downloadBlob(blob, filename){
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = filename; document.body.appendChild(a); a.click();
  setTimeout(()=>{ URL.revokeObjectURL(url); a.remove(); }, 1000);
}

async function generatePdfBlob(){
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF({unit:'pt',format:'a4'});
  doc.setFontSize(16);
  doc.addImage(logoBase64, 'PNG', 40, 30, 80, 30);
  doc.text('Báo cáo Kho 705', 140, 50);
  doc.setFontSize(10);
  let y = 90;
  const rows = currentFiltered.slice(0, 500);
  rows.forEach(r=>{
    const t = new Date(r.timeISO).toLocaleString();
    const line = `${t} | ${r.loai} | ${r.ten} | ${r.sl} | ${r.doi||''} | ${r.cate||''} | ${r.user||''}`;
    doc.text(line, 40, y);
    y += 12;
    if (y > 750) { doc.addPage(); y = 40; }
  });
  const uint8 = doc.output('arraybuffer');
  return new Blob([uint8], {type:'application/pdf'});
}

/* ---------- Charts ---------- */
function updateCharts(){
  // stock by category
  const cats = ["Phân bón","Vật tư","Thuốc BVTV","Cà phê"];
  const stockVals = cats.map(cat => kho.filter(i=>i.cate===cat).reduce((s,i)=>s+i.sl,0));
  const ctx1 = document.getElementById("stockChart").getContext('2d');
  if (stockChart) {
    stockChart.data.datasets[0].data = stockVals; stockChart.update();
  } else {
    stockChart = new Chart(ctx1, { type:'bar', data:{labels:cats,datasets:[{label:'Tồn',data:stockVals}]}, options:{responsive:true,maintainAspectRatio:false} });
  }
  // export by team (sum of Xuất)
  const teams = ["Đội 2","Đội 4","Đội 7","Đội 10","Ngoài"];
  const vals = teams.map(t => lichSu.filter(x=>x.loai==="Xuất" && x.doi===t).reduce((s,x)=>s+x.sl,0));
  const ctx2 = document.getElementById("exportChart").getContext('2d');
  if (exportChart) { exportChart.data.datasets[0].data = vals; exportChart.update(); }
  else exportChart = new Chart(ctx2, { type:'pie', data:{labels:teams,datasets:[{data:vals}]}, options:{responsive:true,maintainAspectRatio:false} });
}

/* ---------- Utilities & Init ---------- */
function renderAll(){
  renderUsers(); renderKho(); resetFilter(); updateCharts();
}
function init(){
  // ensure users exist already handled above
  renderAll();
  // optionally auto-login admin for testing - commented out
  // currentUser = users[0]; document.getElementById("loginCard").classList.add("hidden"); document.getElementById("app").classList.remove("hidden");
}
init();
</script>

</body>
</html>