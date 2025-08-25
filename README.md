<!DOCTYPE html>
<html b:version='2' class='v2' expr:dir='data:blog.languageDirection' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
  <meta content='width=device-width, initial-scale=1.0' name='viewport'/>
  <title>Quản lý kho - Đội 2, 4, 7, 10, Ngoài</title>
  <b:include data='blog' name='all-head-content'/>
  <!-- Bootstrap CSS -->
  <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'/>
  <!-- Thư viện SheetJS và jsPDF -->
  <script src='https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js'></script>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js'></script>
  <!-- MD5 cho mã hóa mật khẩu -->
  <script src='https://cdnjs.cloudflare.com/ajax/libs/blueimp-md5/2.18.0/js/md5.min.js'></script>
  <style>
    body {
      background-color: #f8f9fa;
      padding: 20px;
    }
    .container {
      max-width: 1200px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .nav-tabs .nav-link {
      font-weight: bold;
    }
    .table th {
      background-color: #007bff;
      color: white;
    }
    #login-section {
      max-width: 400px;
      margin: 50px auto;
    }
    .alert {
      margin-top: 20px;
    }
    @media (max-width: 576px) {
      .container {
        padding: 10px;
      }
      .nav-tabs .nav-link {
        font-size: 14px;
      }
    }
  </style>
</head>
<body>
  <div class='container'>
    <h1 class='text-center mb-4'>Quản lý kho</h1>
    <!-- Đăng nhập -->
    <div id='login-section' class='card p-4'>
      <h2 class='text-center'>Đăng nhập</h2>
      <div class='mb-3'>
        <label for='username' class='form-label'>Tên đăng nhập</label>
        <input id='username' class='form-control' type='text' placeholder='admin'/>
      </div>
      <div class='mb-3'>
        <label for='password' class='form-label'>Mật khẩu</label>
        <input id='password' class='form-control' type='password' placeholder='password'/>
      </div>
      <button class='btn btn-primary w-100' onclick='login()'>Đăng nhập</button>
    </div>
    <!-- Nội dung chính -->
    <div id='main-section' class='hidden'>
      <ul class='nav nav-tabs mb-4'>
        <li class='nav-item'>
          <a class='nav-link active' href='javascript:void(0)' onclick='showSection("nhap-kho")'>Nhập kho</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link' href='javascript:void(0)' onclick='showSection("xuat-kho")'>Xuất kho</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link' href='javascript:void(0)' onclick='showSection("lich-su")'>Lịch sử</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link' href='javascript:void(0)' onclick='showSection("bao-cao")'>Báo cáo</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link text-danger' href='javascript:void(0)' onclick='logout()'>Đăng xuất</a>
        </li>
      </ul>
      <!-- Nhập kho -->
      <div id='nhap-kho' class='section'>
        <h2>Nhập kho</h2>
        <div class='mb-3'>
          <label for='item-name-nhap' class='form-label'>Tên hàng</label>
          <input id='item-name-nhap' class='form-control' type='text' placeholder='Nhập tên hàng'/>
        </div>
        <div class='mb-3'>
          <label for='quantity-nhap' class='form-label'>Số lượng</label>
          <input id='quantity-nhap' class='form-control' type='number' min='1' placeholder='Nhập số lượng'/>
        </div>
        <div class='mb-3'>
          <label for='team-nhap' class='form-label'>Đội</label>
          <select id='team-nhap' class='form-select'>
            <option value='Đội 2'>Đội 2</option>
            <option value='Đội 4'>Đội 4</option>
            <option value='Đội 7'>Đội 7</option>
            <option value='Đội 10'>Đội 10</option>
            <option value='Ngoài'>Ngoài</option>
          </select>
        </div>
        <button class='btn btn-success' onclick='nhapKho()'>Nhập kho</button>
      </div>
      <!-- Xuất kho -->
      <div id='xuat-kho' class='section hidden'>
        <h2>Xuất kho</h2>
        <div class='mb-3'>
          <label for='item-name-xuat' class='form-label'>Tên hàng</label>
          <input id='item-name-xuat' class='form-control' type='text' placeholder='Nhập tên hàng'/>
        </div>
        <div class='mb-3'>
          <label for='quantity-xuat' class='form-label'>Số lượng</label>
          <input id='quantity-xuat' class='form-control' type='number' min='1' placeholder='Nhập số lượng'/>
        </div>
        <div class='mb-3'>
          <label for='team-xuat' class='form-label'>Đội</label>
          <select id='team-xuat' class='form-select'>
            <option value='Đội 2'>Đội 2</option>
            <option value='Đội 4'>Đội 4</option>
            <option value='Đội 7'>Đội 7</option>
            <option value='Đội 10'>Đội 10</option>
            <option value='Ngoài'>Ngoài</option>
          </select>
        </div>
        <button class='btn btn-success' onclick='xuatKho()'>Xuất kho</button>
      </div>
      <!-- Lịch sử -->
      <div id='lich-su' class='section hidden'>
        <h2>Lịch sử giao dịch</h2>
        <div class='mb-3'>
          <label for='search-input' class='form-label'>Tìm kiếm</label>
          <input id='search-input' class='form-control' type='text' onkeyup='searchHistory()' placeholder='Nhập tên hàng hoặc đội'/>
        </div>
        <table class='table table-bordered'>
          <thead>
            <tr>
              <th>Thời gian</th>
              <th>Loại</th>
              <th>Tên hàng</th>
              <th>Số lượng</th>
              <th>Đội</th>
            </tr>
          </thead>
          <tbody id='history-body'></tbody>
        </table>
      </div>
      <!-- Báo cáo -->
      <div id='bao-cao' class='section hidden'>
        <h2>Báo cáo tồn kho</h2>
        <table class='table table-bordered'>
          <thead>
            <tr>
              <th>Tên hàng</th>
              <th>Số lượng</th>
              <th>Đội</th>
            </tr>
          </thead>
          <tbody id='report-body'></tbody>
        </table>
        <button class='btn btn-primary me-2' onclick='exportExcel()'>Xuất Excel</button>
        <button class='btn btn-primary' onclick='exportPDF()'>Xuất PDF</button>
      </div>
    </div>
  </div>
  <!-- Bootstrap JS -->
  <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'></script>
  <!-- JavaScript -->
  <script>
    // Khởi tạo dữ liệu mặc định
    const ADMIN_CREDENTIALS = {
      username: 'admin',
      password: md5('password') // Mật khẩu mã hóa MD5
    };

    // Kiểm tra đăng nhập
    function login() {
      const username = document.getElementById('username').value;
      const password = md5(document.getElementById('password').value);
      if (username === ADMIN_CREDENTIALS.username && password === ADMIN_CREDENTIALS.password) {
        localStorage.setItem('isLoggedIn', 'true');
        document.getElementById('login-section').classList.add('hidden');
        document.getElementById('main-section').classList.remove('hidden');
        showSection('nhap-kho');
        loadHistory();
        loadReport();
      } else {
        showAlert('Sai tên đăng nhập hoặc mật khẩu!', 'danger');
      }
    }

    // Đăng xuất
    function logout() {
      localStorage.removeItem('isLoggedIn');
      document.getElementById('login-section').classList.remove('hidden');
      document.getElementById('main-section').classList.add('hidden');
      document.getElementById('username').value = '';
      document.getElementById('password').value = '';
    }

    // Kiểm tra trạng thái đăng nhập
    window.onload = function() {
      if (localStorage.getItem('isLoggedIn') === 'true') {
        document.getElementById('login-section').classList.add('hidden');
        document.getElementById('main-section').classList.remove('hidden');
        showSection('nhap-kho');
        loadHistory();
        loadReport();
      }
    };

    // Hiển thị section
    function showSection(sectionId) {
      document.querySelectorAll('.section').forEach(section => {
        section.classList.add('hidden');
      });
      document.getElementById(sectionId).classList.remove('hidden');
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
      });
      document.querySelector(`[onclick="showSection('${sectionId}')"]`).classList.add('active');
    }

    // Hiển thị thông báo
    function showAlert(message, type) {
      const alertDiv = document.createElement('div');
      alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
      alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      `;
      document.querySelector('.container').prepend(alertDiv);
      setTimeout(() => alertDiv.remove(), 3000);
    }

    // Nhập kho
    function nhapKho() {
      const itemName = document.getElementById('item-name-nhap').value.trim();
      const quantity = parseInt(document.getElementById('quantity-nhap').value);
      const team = document.getElementById('team-nhap').value;
      if (!itemName || isNaN(quantity) || quantity <= 0) {
        showAlert('Vui lòng nhập đầy đủ và đúng thông tin!', 'danger');
        return;
      }
      const inventory = JSON.parse(localStorage.getItem('inventory') || '[]');
      const existingItem = inventory.find(item => item.name === itemName && item.team === team);
      if (existingItem) {
        existingItem.quantity += quantity;
      } else {
        inventory.push({ name: itemName, quantity: quantity, team: team });
      }
      localStorage.setItem('inventory', JSON.stringify(inventory));
      const history = JSON.parse(localStorage.getItem('history') || '[]');
      history.push({
        time: new Date().toLocaleString('vi-VN'),
        type: 'Nhập',
        name: itemName,
        quantity: quantity,
        team: team
      });
      localStorage.setItem('history', JSON.stringify(history));
      showAlert('Nhập kho thành công!', 'success');
      loadHistory();
      loadReport();
      document.getElementById('item-name-nhap').value = '';
      document.getElementById('quantity-nhap').value = '';
    }

    // Xuất kho
    function xuatKho() {
      const itemName = document.getElementById('item-name-xuat').value.trim();
      const quantity = parseInt(document.getElementById('quantity-xuat').value);
      const team = document.getElementById('team-xuat').value;
      if (!itemName || isNaN(quantity) || quantity <= 0) {
        showAlert('Vui lòng nhập đầy đủ và đúng thông tin!', 'danger');
        return;
      }
      const inventory = JSON.parse(localStorage.getItem('inventory') || '[]');
      const existingItem = inventory.find(item => item.name === itemName && item.team === team);
      if (!existingItem || existingItem.quantity < quantity) {
        showAlert('Hàng không đủ hoặc không tồn tại!', 'danger');
        return;
      }
      existingItem.quantity -= quantity;
      if (existingItem.quantity === 0) {
        const index = inventory.indexOf(existingItem);
        inventory.splice(index, 1);
      }
      localStorage.setItem('inventory', JSON.stringify(inventory));
      const history = JSON.parse(localStorage.getItem('history') || '[]');
      history.push({
        time: new Date().toLocaleString('vi-VN'),
        type: 'Xuất',
        name: itemName,
        quantity: quantity,
        team: team
      });
      localStorage.setItem('history', JSON.stringify(history));
      showAlert('Xuất kho thành công!', 'success');
      loadHistory();
      loadReport();
      document.getElementById('item-name-xuat').value = '';
      document.getElementById('quantity-xuat').value = '';
    }

    // Tải lịch sử
    function loadHistory() {
      const history = JSON.parse(localStorage.getItem('history') || '[]');
      const historyBody = document.getElementById('history-body');
      historyBody.innerHTML = '';
      history.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.time}</td>
          <td>${item.type}</td>
          <td>${item.name}</td>
          <td>${item.quantity}</td>
          <td>${item.team}</td>
        `;
        historyBody.appendChild(row);
      });
    }

    // Tìm kiếm lịch sử
    function searchHistory() {
      const keyword = document.getElementById('search-input').value.toLowerCase();
      const history = JSON.parse(localStorage.getItem('history') || '[]');
      const filtered = history.filter(item => 
        item.name.toLowerCase().includes(keyword) || 
        item.team.toLowerCase().includes(keyword)
      );
      const historyBody = document.getElementById('history-body');
      historyBody.innerHTML = '';
      filtered.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.time}</td>
          <td>${item.type}</td>
          <td>${item.name}</td>
          <td>${item.quantity}</td>
          <td>${item.team}</td>
        `;
        historyBody.appendChild(row);
      });
    }

    // Tải báo cáo
    function loadReport() {
      const inventory = JSON.parse(localStorage.getItem('inventory') || '[]');
      const reportBody = document.getElementById('report-body');
      reportBody.innerHTML = '';
      inventory.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.name}</td>
          <td>${item.quantity}</td>
          <td>${item.team}</td>
        `;
        reportBody.appendChild(row);
      });
    }

    // Xuất Excel
    function exportExcel() {
      const inventory = JSON.parse(localStorage.getItem('inventory') || '[]');
      const ws = XLSX.utils.json_to_sheet(inventory.map(item => ({
        'Tên hàng': item.name,
        'Số lượng': item.quantity,
        'Đội': item.team
      })));
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, 'Báo cáo tồn kho');
      XLSX.write(wb, 'BaoCaoTonKho.xlsx');
    }

    // Xuất PDF
    function exportPDF() {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();
      doc.setFontSize(16);
      doc.text('Báo cáo tồn kho', 20, 20);
      doc.setFontSize(12);
      doc.text('Ngày: ' + new Date().toLocaleString('vi-VN'), 20, 30);
      let y = 50;
      doc.text('Tên hàng', 20, y);
      doc.text('Số lượng', 80, y);
      doc.text('Đội', 120, y);
      doc.line(20, y + 2, 190, y + 2);
      y += 10;
      const inventory = JSON.parse(localStorage.getItem('inventory') || '[]');
      inventory.forEach(item => {
        doc.text(item.name, 20, y);
        doc.text(item.quantity.toString(), 80, y);
        doc.text(item.team, 120, y);
        y += 10;
      });
      doc.save('BaoCaoTonKho.pdf');
    }
  </script>
</body>
</html>