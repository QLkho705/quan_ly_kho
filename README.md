<!DOCTYPE html>
<html>
<head><title>Trang chủ - Kho 705</title></head>
<body>
  <h2>Chào mừng Admin</h2>
  <ul>
    <li><a href="{{ url_for('nhap') }}">➕ Nhập kho</a></li>
    <li><a href="{{ url_for('xuat') }}">➖ Xuất kho</a></li>
    <li><a href="{{ url_for('lichsu') }}">📜 Lịch sử</a></li>
    <li><a href="{{ url_for('baocao') }}">📊 Báo cáo</a></li>
    <li><a href="{{ url_for('logout') }}">🚪 Đăng xuất</a></li>
  </ul>
</body>
</html>