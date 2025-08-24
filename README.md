* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; background: #f6f7f8; color: #142; }
.topbar { position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: #0a7a2f; color: #fff; }
.brand { display: flex; align-items: center; gap: 10px; }
.logo { display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 8px; background: #fff; color: #0a7a2f; font-weight: 800; }
.title { font-weight: 700; }
.nav a { color: #eaffea; text-decoration: none; margin-left: 10px; font-weight: 600; }
.container { max-width: 920px; margin: 18px auto; padding: 0 12px; }
.card { background: #fff; border: 1px solid #e6e8ea; border-radius: 10px; padding: 16px; margin-bottom: 16px; box-shadow: 0 1px 2px rgba(0,0,0,.04); }
.row { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }
.row input { flex: 1; padding: 10px 12px; border: 1px solid #cfd6cf; border-radius: 8px; }
button { padding: 10px 14px; border: 0; border-radius: 8px; font-weight: 700; cursor: pointer; background: #0a7a2f; color: #fff; }
button:disabled { opacity: .6; cursor: not-allowed; }
.table { width: 100%; border-collapse: collapse; margin-top: 8px; }
.table th, .table td { padding: 10px; border-bottom: 1px solid #eef1f2; text-align: left; }
.status { margin-left: 10px; font-size: 14px; }
.footer { text-align: center; color: #678; padding: 30px 0 60px; }
.tip { background: #e7f7ec; border: 1px dashed #b7e3c6; color: #064b24; padding: 8px 10px; border-radius: 8px; margin-top: 8px; }