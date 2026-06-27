# Thông tin chung
- Họ và tên: Lưu Huy Hoàng
- MSSV: 23127047

# FR-01: Đăng ký tài khoản
- Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu.
- Email phải có định dạng hợp lệ (user@domain.com) và là duy nhất trong hệ thống.
- Yêu cầu mật khẩu mạnh: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (@, $, !, %, *, ?, &).
- Phải có trường Xác nhận mật khẩu — hệ thống từ chối nếu hai trường không khớp.
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

## Domain Testing

### Giải thích

Đối với FR-01: Đăng ký tài khoản, các biến đầu vào cần được bóc tách theo đúng đặc tả như sau:

1. **Họ Tên**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập, không được rỗng.
   - Miền hợp lệ: Bất kỳ chuỗi không rỗng nào biểu diễn họ tên người dùng, ví dụ "Nguyen Van A".
   - Miền không hợp lệ: Chuỗi rỗng, hoặc bỏ trống trường.

2. **Email**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập, phải có định dạng hợp lệ theo mẫu `user@domain.com`, và phải là duy nhất trong hệ thống.
   - Miền hợp lệ: Chuỗi có cấu trúc email đúng cú pháp và chưa tồn tại trong hệ thống, ví dụ "user01@test.com".
   - Miền không hợp lệ: Chuỗi sai định dạng email, ví dụ thiếu ký tự `@`, thiếu phần domain, hoặc email đã được đăng ký trước đó.

3. **Mật khẩu**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập, tối thiểu 8 ký tự, phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt thuộc tập `@`, `$`, `!`, `%`, `*`, `?`, `&`.
   - Miền hợp lệ: Chuỗi đáp ứng đồng thời tất cả điều kiện trên, ví dụ "P@ssw0rd".
   - Miền không hợp lệ: Chuỗi ngắn hơn 8 ký tự, hoặc thiếu một trong bốn nhóm ký tự bắt buộc.

4. **Xác nhận mật khẩu**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập và phải khớp tuyệt đối với trường Mật khẩu.
   - Miền hợp lệ: Giá trị trùng hoàn toàn với Mật khẩu.
   - Miền không hợp lệ: Giá trị khác Mật khẩu dù chỉ khác 1 ký tự.

Từ phân tích trên, logic nghiệp vụ chính cần kiểm tra là: tất cả trường bắt buộc phải được nhập đầy đủ, email phải đúng định dạng và chưa tồn tại, mật khẩu phải thỏa toàn bộ chính sách an toàn, xác nhận mật khẩu phải khớp, và khi mọi điều kiện đều hợp lệ thì hệ thống phải chuyển người dùng tới trang Đăng nhập sau khi đăng ký thành công.

### Domain Test Cases

| Test Case ID | Description | Pre-condition | Input Data | Test Steps | Expected Result | Actual Result | Status | Defect ID | Tested By | Date Tested |
| ------------ | ----------- | ------------- | ---------- | ---------- | --------------- | ------------- | ------ | --------- | --------- | ----------- |
| FR-01-DT-01  | Đăng ký thành công với toàn bộ dữ liệu hợp lệ | Email "fr01.dt01@test.com" chưa tồn tại trong hệ thống. | Họ Tên: Nguyen Van A<br>Email: fr01.dt01@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt01@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Đăng ký thành công và hệ thống chuyển sang trang Đăng nhập. | Vẫn báo lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Failed | BUG-FR01-01| Hoang | 24/06/2026 |
| FR-01-DT-02  | Từ chối khi Họ Tên bị bỏ trống | Không yêu cầu. | Họ Tên: <br>Email: fr01.dt02@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang Đăng ký tài khoản.<br>2. Để trống trường Họ Tên.<br>3. Nhập "fr01.dt02@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi bắt buộc nhập Họ Tên và không cho phép gửi form. | Hiển thị lỗi bắt buộc nhập Họ Tên và không cho phép gửi form. | Passed | | Hoang | 25/06/2026 |
| FR-01-DT-03  | Từ chối khi Email sai định dạng do thiếu ký tự @ | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt03.test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt03.test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi định dạng Email không hợp lệ và không cho phép gửi form. | Hiển thị lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." không khớp với mong đợi | Failed | BUG-FR01-02 | Hoang | 25/06/2026 |
| FR-01-DT-04  | Từ chối khi Email đã tồn tại trong hệ thống | Đã tồn tại một tài khoản đăng ký thành công với Email "fr01.existing@test.com" trong cơ sở dữ liệu. | Họ Tên: Nguyen Van A<br>Email: fr01.existing@test.com<br>Mật khẩu: My Password 123<br>Xác nhận mật khẩu: My Password 123 | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.existing@test.com" vào trường Email.<br>4. Nhập "My Password 123" vào trường Mật khẩu.<br>5. Nhập "My Password 123" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Email đã được sử dụng và không cho phép tạo tài khoản mới. | Vẫn đăng ký thành công và hệ thống chuyển sang trang Đăng nhập. | Failed | BUG-FR01-03 | Hoang | 25/06/2026 |
| FR-01-DT-05  | Từ chối khi Mật khẩu chỉ có 7 ký tự | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt05@test.com<br>Mật khẩu: P@ssw0r<br>Xác nhận mật khẩu: P@ssw0r | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt05@test.com" vào trường Email.<br>4. Nhập "P@ssw0r" vào trường Mật khẩu.<br>5. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Mật khẩu phải có tối thiểu 8 ký tự. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Passed | | Hoang | 25/06/2026 |
| FR-01-DT-06  | Từ chối khi Mật khẩu thiếu chữ hoa | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt06@test.com<br>Mật khẩu: p@ssw0rd<br>Xác nhận mật khẩu: p@ssw0rd | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt06@test.com" vào trường Email.<br>4. Nhập "p@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "p@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ hoa. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Passed | | Hoang | 25/06/2026 |
| FR-01-DT-07  | Từ chối khi Mật khẩu thiếu chữ thường | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt07@test.com<br>Mật khẩu: P@SSW0RD<br>Xác nhận mật khẩu: P@SSW0RD | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt07@test.com" vào trường Email.<br>4. Nhập "P@SSW0RD" vào trường Mật khẩu.<br>5. Nhập "P@SSW0RD" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ thường. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Passed | | Hoang | 25/06/2026 |
| FR-01-DT-08  | Từ chối khi Mật khẩu thiếu chữ số | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt08@test.com<br>Mật khẩu: P@ssword<br>Xác nhận mật khẩu: P@ssword | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt08@test.com" vào trường Email.<br>4. Nhập "P@ssword" vào trường Mật khẩu.<br>5. Nhập "P@ssword" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ số. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Passed | | Hoang | 25/06/2026 |
| FR-01-DT-09  | Từ chối khi Mật khẩu thiếu ký tự đặc biệt | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt09@test.com<br>Mật khẩu: Password1<br>Xác nhận mật khẩu: Password1 | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt09@test.com" vào trường Email.<br>4. Nhập "Password1" vào trường Mật khẩu.<br>5. Nhập "Password1" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Mật khẩu phải có ít nhất 1 ký tự đặc biệt hợp lệ. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Passed | | Hoang | 25/06/2026 |
| FR-01-DT-10  | Từ chối khi Xác nhận mật khẩu không khớp | Không yêu cầu. | Họ Tên: Nguyen Van A<br>Email: fr01.dt10@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rD | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt10@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rD" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Xác nhận mật khẩu không khớp với Mật khẩu. | UI không có field để điền trường "Xác nhận mật khẩu" | Failed | BUG-FR01-04 | Hoang | 25/06/2026 |
## Boundary Value Analysis

### Giải thích

Trong FR-01, các ràng buộc có tính chất biên và có thể lượng hóa bằng số xuất hiện hoặc độ dài chuỗi gồm:

1. **Độ dài Mật khẩu**
   - Ràng buộc tối thiểu: 8 ký tự.
   - Điểm biên cần xét: 7 ký tự, 8 ký tự, 9 ký tự.
   - Tại $n = 7$, hệ thống phải từ chối vì nhỏ hơn ngưỡng tối thiểu.
   - Tại $n = 8$, hệ thống phải chấp nhận nếu các điều kiện thành phần khác đều hợp lệ.
   - Tại $n = 9$, hệ thống vẫn phải chấp nhận nếu các điều kiện thành phần khác đều hợp lệ.

2. **Số lượng chữ hoa trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 chữ hoa.
   - Điểm biên cần xét: 0 chữ hoa, 1 chữ hoa, 2 chữ hoa.
   - $0$ là vùng không hợp lệ ngay dưới ngưỡng.
   - $1$ là ngưỡng hợp lệ tối thiểu.
   - $2$ là vùng hợp lệ phía trên ngưỡng.

3. **Số lượng chữ thường trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 chữ thường.
   - Điểm biên cần xét: 0 chữ thường, 1 chữ thường, 2 chữ thường.

4. **Số lượng chữ số trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 chữ số.
   - Điểm biên cần xét: 0 chữ số, 1 chữ số, 2 chữ số.

5. **Số lượng ký tự đặc biệt trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 ký tự đặc biệt thuộc tập `@`, `$`, `!`, `%`, `*`, `?`, `&`.
   - Điểm biên cần xét: 0 ký tự đặc biệt, 1 ký tự đặc biệt, 2 ký tự đặc biệt.

Từ góc nhìn kiểm thử, các điểm 0, 1 và 2 là vùng nhạy cảm vì lỗi thường phát sinh tại ngưỡng tối thiểu: lập trình viên có thể so sánh sai điều kiện "lớn hơn" với "lớn hơn hoặc bằng", hoặc đếm sai số lượng ký tự ở đúng ngưỡng chuyển trạng thái hợp lệ. Khi kiểm tra biên của một biến, các trường bắt buộc khác trên form phải luôn được điền bằng giá trị hợp lệ để cô lập lỗi.

### Boundary Test Cases

| Test Case ID | Description | Pre-condition | Input Data | Test Steps | Expected Result | Actual Result | Status | Defect ID | Tested By | Date Tested |
| ------------ | ----------- | ------------- | ---------- | ---------- | --------------- | ------------- | ------ | --------- | --------- | ----------- |
| FR-01-BVA-01 | Kiểm tra Mật khẩu tại biên dưới với 7 ký tự | Email "fr01.bva01@test.com" chưa tồn tại trong hệ thống. | Họ Tên: Nguyen Van A<br>Email: fr01.bva01@test.com<br>Mật khẩu: P@ssw0r (7 ký tự)<br>Xác nhận mật khẩu: P@ssw0r (7 ký tự) | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva01@test.com" vào trường Email.<br>4. Nhập "P@ssw0r" vào trường Mật khẩu.<br>5. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hệ thống từ chối vì độ dài mật khẩu chỉ đạt 7 ký tự, nhỏ hơn ngưỡng tối thiểu 8 ký tự. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Passed | | Hoang | 25/06/2026 |
| FR-01-BVA-02 | Kiểm tra Mật khẩu tại biên với 8 ký tự | Email "fr01.bva02@test.com" chưa tồn tại trong hệ thống. | Họ Tên: Nguyen Van A<br>Email: fr01.bva02@test.com<br>Mật khẩu: P@ssw0rd (8 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd (8 ký tự) | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva02@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hệ thống chấp nhận vì mật khẩu đạt đúng ngưỡng tối thiểu 8 ký tự và thỏa các điều kiện thành phần bắt buộc. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Failed | BUG-FR01-05 | Hoang | 25/06/2026 |
| FR-01-BVA-03 | Kiểm tra Mật khẩu tại biên trên với 9 ký tự | Email "fr01.bva03@test.com" chưa tồn tại trong hệ thống. | Họ Tên: Nguyen Van A<br>Email: fr01.bva03@test.com<br>Mật khẩu: P@ssw0rd1 (9 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd1 (9 ký tự) | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva03@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd1" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd1" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hệ thống chấp nhận vì mật khẩu vượt qua ngưỡng tối thiểu và vẫn thỏa toàn bộ điều kiện bảo mật. | Hiện lỗi "Mật khẩu quá yếu! Phải dài tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số và KÝ TỰ ĐẶC BIỆT." | Failed | BUG-FR01-06 | Hoang | 25/06/2026 |


## AI Gap Analysis
1. BVA-04 đến BVA-07 trùng lặp với DT-06 đến DT-09
- Bốn test case BVA-04, BVA-05, BVA-06, BVA-07 có input data và expected result trùng hoàn toàn với DT-06, DT-07, DT-08, DT-09:

    - FR-01-BVA-04 (0 chữ hoa) ← trùng FR-01-DT-06
    - FR-01-BVA-05 (0 chữ thường) ← trùng FR-01-DT-07
    - FR-01-BVA-06 (0 chữ số) ← trùng FR-01-DT-08
    - FR-01-BVA-07 (0 ký tự đặc biệt) ← trùng FR-01-DT-09

- Về bản chất, kiểm tra "0 chữ hoa/thường/số/đặc biệt" là phân hoạch miền không hợp lệ (Invalid Partition) — thuộc Domain Testing, không phải BVA. AI đã xếp nhầm chúng vào BVA để đủ số lượng tối thiểu 6-9 cases theo yêu cầu trong prompt (do prompt lúc chạy Function này của em chưa đủ tối ưu), thay vì chỉ giữ 3 case biên độ dài mật khẩu thực sự thuộc BVA.

# FR-10: Trạng thái Đơn hàng (Order State Machine)
Đơn hàng có 5 trạng thái và phải tuân theo sơ đồ chuyển đổi sau:
```text
                 [Admin xác nhận]          [Admin giao hàng]      [Admin hoàn tất]
  ┌──────────┐ ─────────────────► ┌───────────┐ ──────────────► ┌──────────┐ ──────────► ┌───────────┐
  │ pending  │                    │ confirmed │                 │ shipping │             │ delivered │
  └──────────┘                    └───────────┘                 └──────────┘             └───────────┘
       │                               │
       │ [User/Admin hủy]              │ [User/Admin hủy]
       ▼                               ▼
  ┌──────────┐                    ┌──────────┐
  │ canceled │                    │ canceled │
  └──────────┘                    └──────────┘
```
Ràng buộc trạng thái kết thúc (Final States):

- Trạng thái delivered và canceled là trạng thái kết thúc — không được phép chuyển sang bất kỳ trạng thái nào khác.
- Khi đơn hàng đã ở trạng thái shipping, User không được phép tự hủy — chỉ Admin mới có thể thao tác.
- Mọi chuyển đổi không hợp lệ phải trả về lỗi với thông báo phù hợp.

## Domain Testing
### Giải thích
Đối với FR-10: Trạng thái Đơn hàng (Order State Machine), các biến đầu vào và ràng buộc nghiệp vụ cần được bóc tách như sau:

1. **current_state**
   - Kiểu dữ liệu: Chuỗi ký tự đại diện cho trạng thái đơn hàng.
   - Miền hợp lệ: `pending`, `confirmed`, `shipping`, `delivered`, `canceled`.
   - Miền không hợp lệ: Bất kỳ giá trị nào khác 5 trạng thái trên, ví dụ `processing`, `done`, `null`, chuỗi rỗng.

2. **action**
   - Kiểu dữ liệu: Chuỗi ký tự đại diện cho hành động thực thi trên đơn hàng.
   - Miền hợp lệ: `xác nhận`, `giao hàng`, `hoàn tất`, `hủy`.
   - Miền không hợp lệ: Bất kỳ giá trị nào khác 4 hành động trên, ví dụ `đóng đơn`, `hoãn`, `chuyển trạng thái`.

3. **actor**
   - Kiểu dữ liệu: Chuỗi ký tự đại diện cho vai trò người thao tác.
   - Miền hợp lệ: `Admin`, `User`.
   - Miền không hợp lệ: Bất kỳ giá trị nào khác 2 vai trò trên, ví dụ `Guest`, `Manager`, `System`.

Các quy tắc nghiệp vụ chính của sơ đồ trạng thái là:

- Từ `pending`, `Admin` có thể thực hiện `xác nhận` để chuyển sang `confirmed`.
- Từ `confirmed`, `Admin` có thể thực hiện `giao hàng` để chuyển sang `shipping`.
- Từ `shipping`, `Admin` có thể thực hiện `hoàn tất` để chuyển sang `delivered`.
- Từ `pending` và `confirmed`, cả `User` lẫn `Admin` đều có thể thực hiện `hủy` để chuyển sang `canceled` theo đặc tả đã cho.
- `delivered` và `canceled` là trạng thái kết thúc, không được phép chuyển sang bất kỳ trạng thái nào khác.
- Khi đơn hàng đã ở trạng thái `shipping`, `User` không được phép tự hủy, chỉ `Admin` mới có thể thao tác theo đặc tả ràng buộc kết thúc của nghiệp vụ.
- Mọi chuyển đổi không hợp lệ phải trả về lỗi với thông báo phù hợp.

Từ phân tích trên, miền hợp lệ là các bộ ba dữ liệu thỏa đúng trạng thái nguồn, hành động được cho phép, và vai trò có quyền thực thi. Miền không hợp lệ là mọi tổ hợp vi phạm một trong ba điều kiện trên hoặc cố gắng chuyển từ trạng thái kết thúc sang một trạng thái khác.

### Domain Test Cases
| Test Case ID | Description | Pre-condition | Input Data | Test Steps | Expected Result | Actual Result | Status | Defect ID | Tested By | Date Tested |
| ------------ | ----------- | ------------- | ---------- | ---------- | --------------- | ------------- | ------ | --------- | --------- | ----------- |
| FR-10-DT-01  | Xác nhận đơn hàng từ `pending` bởi `Admin` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `pending`. | current_state: pending<br>action: xác nhận<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Chọn hành động `xác nhận`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `pending` sang `confirmed`. | Đơn hàng chuyển từ `pending` sang `confirmed`. | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-02  | Giao hàng đơn từ `confirmed` bởi `Admin` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `confirmed`. | current_state: confirmed<br>action: giao hàng<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Chọn hành động `giao hàng`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `confirmed` sang `shipping`. | Đơn hàng chuyển từ `confirmed` sang `shipping`. | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-03  | Hoàn tất đơn từ `shipping` bởi `Admin` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `shipping`. | current_state: shipping<br>action: hoàn tất<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hoàn tất`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `shipping` sang `delivered`. | Đơn hàng chuyển từ `shipping` sang `delivered`. | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-04  | Hủy đơn từ `pending` bởi `User` | Đã đăng nhập tài khoản User. Tồn tại một đơn hàng của User này đang ở trạng thái `pending`. | current_state: pending<br>action: hủy<br>actor: User | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `User`. | Đơn hàng chuyển từ `pending` sang `canceled`. | Khi User từ UI bấm `Xóa`, đơn hàng biến mất khỏi giao diện của User. Nhưng ở UI của admin, đơn hàng đó vẫn đang ở trạng thái mà UI hiển thị là `Chờ xác nhận` và Admin vẫn có thể bấm `Xác nhận` để process tiếp. | Failed | BUG-FR10-01 | Hoang | 27/06/2026 |
| FR-10-DT-05  | Hủy đơn từ `pending` bởi `Admin` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `pending`. | current_state: pending<br>action: hủy<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `pending` sang `canceled`. | Đơn hàng chuyển từ `pending` sang `canceled`. | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-06  | Hủy đơn từ `confirmed` bởi `User` | Đã đăng nhập tài khoản User. Tồn tại một đơn hàng của User này đang ở trạng thái `confirmed`. | current_state: confirmed<br>action: hủy<br>actor: User | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `User`. | Đơn hàng chuyển từ `confirmed` sang `canceled`. | Khi Admin thực hiện `Xác nhận`, đơn hàng chuyển state sang `Confirmed`. Đơn hàng đó đồng thời biến mất khỏi UI của User -> Không thể `Hủy` từ phía User khi đơn hàng ở state `Confirmed`| Failed | BUG-FR10-02 | Hoang | 27/06/2026 |
| FR-10-DT-07  | Hủy đơn từ `confirmed` bởi `Admin` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `confirmed`. | current_state: confirmed<br>action: hủy<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `confirmed` sang `canceled`. | Đơn hàng chuyển từ `confirmed` sang `canceled`. | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-08  | User cố hủy đơn ở trạng thái `shipping` | Đã đăng nhập tài khoản User. Tồn tại một đơn hàng của User này đang ở trạng thái `shipping`. | current_state: shipping<br>action: hủy<br>actor: User | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `User`. | Trả về lỗi, không cho phép `User` tự hủy đơn ở trạng thái `shipping`. | UI của User không hiện đơn hàng khi đơn hàng ở trạng thái `shipping` -> Không thể thực hiện `Hủy` | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-09  | Admin cố hủy đơn ở trạng thái `shipping` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `shipping`. | current_state: shipping<br>action: hủy<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `shipping` sang `canceled`. | UI của Admin không hiện nút `Hủy` khi đơn hàng ở trạng thái `Shipping` -> Không thể thực hiện `Hủy`| Failed | BUG-FR10-03 | Hoang | 27/06/2026 |
| FR-10-DT-10  | Cố xác nhận đơn đã `delivered` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `delivered`. | current_state: delivered<br>action: xác nhận<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `delivered`.<br>3. Chọn hành động `xác nhận`.<br>4. Thực thi thao tác với vai trò `Admin`. | Trả về lỗi vì `delivered` là trạng thái kết thúc, không được chuyển tiếp. | Khi 1 đơn hàng ở trạng thái `delivered`, UI của Admin không hiện bất kỳ nút nào -> Không thể thực hiện hành động `xác nhận` | Passed | | Hoang | 27/06/2026 |
| FR-10-DT-11  | Cố giao hàng đơn đã `canceled` | Đã đăng nhập tài khoản Admin. Tồn tại một đơn hàng đang ở trạng thái `canceled`. | current_state: canceled<br>action: giao hàng<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `canceled`.<br>3. Chọn hành động `giao hàng`.<br>4. Thực thi thao tác với vai trò `Admin`. | Trả về lỗi vì `canceled` là trạng thái kết thúc, không được chuyển tiếp. | Khi 1 đơn hàng ở trạng thái `canceled`, UI của Admin vẫn hiện nút `Đánh dấu Đã giao` (hành vi sai). Sau khi bấm nút đó, trạng thái của đơn hàng chuyển sang `delivered` (hành vi sai do trước đó `canceled` đã là trạng thái kết thúc) | Failed | BUG-FR10-04 | Hoang | 27/06/2026 |

## Boundary Value Analysis
### Giải thích
Đối với FR-10, không có biến đầu vào nào mang tính chất số học hoặc độ dài chuỗi được đặc tả rõ để áp dụng Boundary Value Analysis theo đúng định nghĩa kỹ thuật.

1. `current_state` là một biến phân loại kiểu enum với tập giá trị cố định gồm 5 trạng thái.
2. `action` là một biến phân loại kiểu enum với tập giá trị cố định gồm 4 hành động.
3. `actor` là một biến phân loại kiểu enum với tập giá trị cố định gồm 2 vai trò.
4. Sơ đồ chuyển đổi trạng thái là bài toán logic trạng thái, không phải bài toán có biên số học hay biên độ dài để kiểm tra theo kiểu `Boundary`, `Boundary - 1`, `Boundary + 1`.
5. Theo quy tắc biên phạm vi nghiêm ngặt của skill, BVA chỉ được áp dụng cho ràng buộc số/độ dài được đặc tả rõ ràng. FR-10 không có ràng buộc như vậy.

Kết luận kiểm thử biên: BVA không áp dụng cho FR-10. Bộ kiểm thử có giá trị thực tế đã được bao phủ đầy đủ bởi Domain Testing ở phần trên.

### Boundary Test Cases
BVA không áp dụng cho FR-10 vì không có ràng buộc số học hoặc độ dài được đặc tả.

## AI Gap Analysis
1. DT-09 hiểu sai spec — Admin hủy từ shipping bị đánh sai Expected Result
- Đây là lỗi do từ mô tả chức năng (spec). Trong spec của FR-10, trong sơ đồ chuyển đổi trạng thái, từ `shipping`, `Admin` chỉ có action `hoàn tất` để chuyển sang `delivered`, không có đường mũi tên nào cho phép `Admin` hủy từ trạng thái `shipping`. 
```text
                 [Admin xác nhận]          [Admin giao hàng]      [Admin hoàn tất]
  ┌──────────┐ ─────────────────► ┌───────────┐ ──────────────► ┌──────────┐ ──────────► ┌───────────┐
  │ pending  │                    │ confirmed │                  │ shipping │             │ delivered │
  └──────────┘                    └───────────┘                  └──────────┘             └───────────┘
       │                               │
       │ [User/Admin hủy]              │ [User/Admin hủy]
       ▼                               ▼
  ┌──────────┐                    ┌──────────┐
  │ canceled │                    │ canceled │
  └──────────┘                    └──────────┘
```
- Tuy nhiên, ở phần mô tả bên dưới lại có **"Khi đơn hàng đã ở trạng thái shipping, User không được phép tự hủy — chỉ Admin mới có thể thao tác."** -> Thực chất `Admin` có thể hủy từ `shipping`.
- Chính sự mâu thuẫn này trong spec đã dẫn đến việc AI tạo ra test case FR-10-DT-09 với Expected Result sai. 

# FR-12: Kiểm soát truy cập (Access Control)
- Phân hệ Admin chỉ dành cho tài khoản có role = 'admin'.
- Tất cả các API Admin (/api/admin/*) và các API có tính ảnh hưởng dữ liệu (POST/PUT/DELETE /api/products, /api/categories, /api/coupons) đều phải yêu cầu:  
   - Token JWT hợp lệ.  
   - role = 'admin' trong Token.

## Domain Testing
### Giải thích

**1. Danh sách các biến đầu vào**

- Đường dẫn API được gọi.
- Phương thức HTTP của yêu cầu.
- Token JWT trong tiêu đề Authorization.
- Giá trị vai trò `role` được nhúng trong token.
- Trạng thái hiệu lực của token, bao gồm còn hạn, hết hạn và chữ ký hợp lệ.

**2. Kiểu dữ liệu và ràng buộc chi tiết**

- Đường dẫn API là chuỗi ký tự và phải khớp đúng một trong hai nhóm quy tắc nghiệp vụ sau:
  - Nhóm 1: mọi API thuộc tiền tố `/api/admin/*`.
  - Nhóm 2: các API có tác động dữ liệu gồm `POST`, `PUT`, `DELETE` trên `/api/products`, `/api/categories`, `/api/coupons`.
- Phương thức HTTP là chuỗi mô tả hành động. Trong phạm vi đặc tả này, các phương thức có ý nghĩa kiểm soát là `POST`, `PUT`, `DELETE` và các phương thức còn lại được xem là ngoài phạm vi tác động dữ liệu.
- Token JWT là chuỗi mang thông tin xác thực. Đặc tả yêu cầu token phải hợp lệ, có chữ ký đúng và còn hiệu lực.
- Vai trò `role` là chuỗi logic trong token. Đặc tả yêu cầu giá trị phải là `admin`.
- Trạng thái token là thuộc tính logic của xác thực. Nếu token không tồn tại, sai định dạng, chữ ký sai hoặc hết hạn thì đều được xem là không hợp lệ.

**3. Quy tắc nghiệp vụ và logic ngầm**

- Mọi chức năng thuộc phân hệ Admin chỉ được phép truy cập nếu token JWT hợp lệ và `role = 'admin'`.
- Mọi API có tác động dữ liệu thuộc nhóm `POST`, `PUT`, `DELETE` trên các tài nguyên `products`, `categories`, `coupons` cũng phải tuân thủ cùng quy tắc xác thực và phân quyền như trên.
- Nếu thiếu token hoặc token không hợp lệ thì hệ thống phải từ chối trước khi xét đến vai trò.
- Nếu token hợp lệ nhưng vai trò không phải `admin` thì hệ thống phải từ chối truy cập dù endpoint là Admin hay là API tác động dữ liệu.
- Nếu token hợp lệ và vai trò là `admin` thì yêu cầu phải được chấp nhận đối với đúng các endpoint nằm trong phạm vi đặc tả.
- Các endpoint không nằm trong phạm vi đặc tả không được suy diễn thêm ràng buộc ngoài những gì đã nêu.

### 2. Domain Test Cases

| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-12-DT-01 | Truy cập API Admin bằng token hợp lệ và vai trò admin | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/users<br>Authorization: Bearer {{admin_token}}<br>Role trong token: admin<br>Trạng thái token: hợp lệ, còn hạn | 1. Mở Postman hoặc Swagger UI.<br>2. Gọi POST /api/login với credentials hợp lệ của tài khoản admin để lấy token thật.<br>3. Chọn phương thức GET cho đường dẫn `/api/admin/users`.<br>4. Thêm tiêu đề `Authorization` với giá trị `Bearer {{admin_token}}`.<br>5. Gửi yêu cầu. | Hệ thống cho phép truy cập và trả về phản hồi thành công theo nghiệp vụ của API. |  |  |  |  |
| FR-12-DT-02 | Truy cập API Admin khi thiếu token JWT | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/users<br>Authorization: rỗng<br>Role trong token: không có<br>Trạng thái token: không tồn tại | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức GET cho đường dẫn `/api/admin/users`.<br>3. Không nhập tiêu đề `Authorization`.<br>4. Gửi yêu cầu. | Hệ thống từ chối truy cập vì thiếu token JWT hợp lệ. |  |  |  |  |
| FR-12-DT-03 | Truy cập API Admin bằng token đã hết hạn | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/users<br>Authorization: Bearer {{expired_admin_token}}<br>Role trong token: admin<br>Trạng thái token: hết hạn | 1. Mở Postman hoặc Swagger UI.<br>2. Lấy một token JWT của admin đã hết hạn (từ phiên đăng nhập cũ hoặc sinh bằng tool giả lập với thời gian hết hạn trong quá khứ).<br>3. Chọn phương thức GET cho đường dẫn `/api/admin/users`.<br>4. Thêm tiêu đề `Authorization` với giá trị `Bearer {{expired_admin_token}}`.<br>5. Gửi yêu cầu. | Hệ thống từ chối truy cập vì token JWT hết hạn. |  |  |  |  |
| FR-12-DT-04 | Truy cập API Admin bằng token hợp lệ nhưng vai trò user | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/users<br>Authorization: Bearer {{user_token}}<br>Role trong token: user<br>Trạng thái token: hợp lệ, còn hạn | 1. Mở Postman hoặc Swagger UI.<br>2. Gọi POST /api/login với credentials hợp lệ của tài khoản USER thường để lấy token thật.<br>3. Chọn phương thức GET cho đường dẫn `/api/admin/users`.<br>4. Thêm tiêu đề `Authorization` với giá trị `Bearer {{user_token}}`.<br>5. Gửi yêu cầu. | Hệ thống từ chối truy cập vì vai trò trong token không phải `admin`. |  |  |  |  |
| FR-12-DT-05 | Gọi API Admin bằng token có chữ ký sai | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/users<br>Authorization: Bearer {{invalid_signature_token}}<br>Role trong token: admin<br>Trạng thái token: chữ ký không hợp lệ | 1. Mở Postman hoặc Swagger UI.<br>2. Gọi POST /api/login với credentials hợp lệ của tài khoản admin để lấy token thật, sau đó cố tình sửa đổi vài ký tự ở phần cuối của token (phần signature).<br>3. Chọn phương thức GET cho đường dẫn `/api/admin/users`.<br>4. Thêm tiêu đề `Authorization` với giá trị `Bearer {{invalid_signature_token}}`.<br>5. Gửi yêu cầu. | Hệ thống từ chối truy cập vì token JWT không hợp lệ do chữ ký sai. |  |  |  |  |

## Boundary Value Analysis
### Giải thích
**1. Kết luận phạm vi biên**

Đặc tả chức năng này không công bố bất kỳ ràng buộc số học, giới hạn độ dài chuỗi, khoảng giá trị tối thiểu hoặc tối đa nào cho các biến đầu vào. Do đó, không có miền biên số học hoặc biên độ dài nào được nêu rõ để áp dụng kỹ thuật Giá trị Biên một cách đúng phạm vi.

**2. Phân tích theo góc nhìn QA**

- Kỹ thuật Giá trị Biên chỉ nên áp dụng khi đặc tả có nêu một giới hạn cụ thể như độ dài tối thiểu, độ dài tối đa, giá trị nhỏ nhất hoặc giá trị lớn nhất.
- Với đặc tả hiện tại, các quy tắc xác thực là quy tắc logic định tính: token phải hợp lệ, vai trò phải là `admin`, endpoint phải thuộc phạm vi bảo vệ.
- Vì không có ngưỡng số học cụ thể nên không thể xác định hợp lệ cho các điểm `Boundary`, `Boundary - 1`, `Boundary + 1` một cách khách quan.
- Nếu tự ý gán ngưỡng cho token, vai trò hoặc endpoint thì sẽ vi phạm quy tắc không suy diễn ngoài đặc tả.

**3. Kết luận kiểm thử biên**

- Không phát hiện biến đầu vào nào có ràng buộc biên được chỉ rõ trong đặc tả.
- Không thiết kế bộ test biên định lượng cho chức năng này.
- Phần kiểm thử phù hợp nhất cho phạm vi này là phân lớp tương đương và kiểm thử logic truy cập.

### Boundary Test Cases
BVA không áp dụng cho FR-12 vì không có ràng buộc số học hoặc độ dài được đặc tả.

## AI Gap Analysis
1. Token JWT trong Input Data không thể dùng trực tiếp để test
- Toàn bộ 10 test cases đều có token JWT hardcode trong cột Input Data, ví dụ `eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4i...abc123signature`. Đây là token AI tự tạo, không có chữ ký hợp lệ từ secret key của SUT. Tester không thể copy-paste token này vào Postman và expect kết quả đúng — tất cả đều sẽ bị từ chối ở bước verify signature, kể cả các case expected là thành công.
- Đây là giới hạn inherent của AI khi xử lý security testing — AI không có khả năng biết secret key của hệ thống đang test, nên không thể sinh ra token có chữ ký thật. AI cần được hướng dẫn thay token bằng placeholder và bổ sung bước đăng nhập lấy token vào Test Steps.

# FR-20: Chọn FR-01: Đăng ký tài khoản nhưng làm ở bản Mobile
- Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu.
- Email phải có định dạng hợp lệ (user@domain.com) và là duy nhất trong hệ thống.
- Yêu cầu mật khẩu mạnh: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (@, $, !, %, *, ?, &).
- Phải có trường Xác nhận mật khẩu — hệ thống từ chối nếu hai trường không khớp.
- Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

## Domain Testing

### Giải thích

Đối với FR-20: Chọn FR-01: Đăng ký tài khoản và làm ở bản Mobile, các biến đầu vào và ràng buộc nghiệp vụ cần được bóc tách như sau:

1. **Họ Tên**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập, không được rỗng.
   - Miền hợp lệ: Bất kỳ chuỗi không rỗng nào biểu diễn họ tên người dùng, ví dụ "Nguyen Van A".
   - Miền không hợp lệ: Chuỗi rỗng, hoặc bỏ trống trường.

2. **Email**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập, phải có định dạng hợp lệ theo mẫu `user@domain.com`, và phải là duy nhất trong hệ thống.
   - Miền hợp lệ: Chuỗi có cấu trúc email đúng cú pháp và chưa tồn tại trong hệ thống, ví dụ "fr20.user01@test.com".
   - Miền không hợp lệ: Chuỗi sai định dạng email, ví dụ thiếu ký tự `@`, thiếu phần domain, hoặc email đã được đăng ký trước đó.

3. **Mật khẩu**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập, tối thiểu 8 ký tự, phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt thuộc tập `@`, `$`, `!`, `%`, `*`, `?`, `&`.
   - Miền hợp lệ: Chuỗi đáp ứng đồng thời tất cả điều kiện trên, ví dụ "P@ssw0rd".
   - Miền không hợp lệ: Chuỗi ngắn hơn 8 ký tự, hoặc thiếu một trong bốn nhóm ký tự bắt buộc.

4. **Xác nhận mật khẩu**
   - Kiểu dữ liệu: Chuỗi ký tự.
   - Ràng buộc: Bắt buộc nhập và phải khớp tuyệt đối với trường Mật khẩu.
   - Miền hợp lệ: Giá trị trùng hoàn toàn với Mật khẩu.
   - Miền không hợp lệ: Giá trị khác Mật khẩu dù chỉ khác 1 ký tự.

5. **Bối cảnh Mobile**
   - Kiểu dữ liệu: Bối cảnh giao diện người dùng.
   - Ràng buộc: Luồng thao tác phải thực hiện được trên màn hình di động với các trường nhập và nút hành động hiển thị rõ ràng.
   - Miền hợp lệ: Người dùng có thể nhập đủ dữ liệu và thực hiện đăng ký thành công trên giao diện mobile.
   - Miền không hợp lệ: Giao diện không hiển thị đủ trường bắt buộc, nút đăng ký không thao tác được, hoặc luồng điều hướng sau đăng ký không chuyển đúng trang Đăng nhập.

Từ phân tích trên, logic nghiệp vụ chính cần kiểm tra là: tất cả trường bắt buộc phải được nhập đầy đủ, email phải đúng định dạng và chưa tồn tại, mật khẩu phải thỏa toàn bộ chính sách an toàn, xác nhận mật khẩu phải khớp, giao diện mobile phải cho phép thao tác đầy đủ trên thiết bị di động, và khi mọi điều kiện đều hợp lệ thì hệ thống phải chuyển người dùng tới trang Đăng nhập sau khi đăng ký thành công.

### Domain Test Cases

| Test Case ID | Description                                                         | Input Data                                                                                                                     | Test Steps                                                                                                                                                                                                                                                                                                            | Expected Result                                                         | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-20-DT-01  | Đăng ký thành công trên giao diện mobile với toàn bộ dữ liệu hợp lệ | Họ Tên: Nguyen Van A<br>Email: fr20.dt01@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt01@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Đăng ký thành công và hệ thống chuyển sang trang Đăng nhập.             |               |        |           |             |
| FR-20-DT-02  | Từ chối khi Họ Tên bị bỏ trống trên mobile                          | Họ Tên: <br>Email: fr20.dt02@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd<br>Bối cảnh: Mobile                 | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Để trống trường Họ Tên.<br>4. Nhập "fr20.dt02@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".                    | Hiển thị lỗi bắt buộc nhập Họ Tên và không cho phép gửi form.           |               |        |           |             |
| FR-20-DT-03  | Từ chối khi Email sai định dạng do thiếu ký tự @                    | Họ Tên: Nguyen Van A<br>Email: fr20.dt03.test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt03.test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hiển thị lỗi định dạng Email không hợp lệ và không cho phép gửi form.   |               |        |           |             |
| FR-20-DT-04  | Từ chối khi Email đã tồn tại trong hệ thống                         | Họ Tên: Nguyen Van A<br>Email: fr20.existing@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd<br>Bối cảnh: Mobile | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.existing@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký". | Hiển thị lỗi Email đã được sử dụng và không cho phép tạo tài khoản mới. |               |        |           |             |
| FR-20-DT-05  | Từ chối khi Mật khẩu chỉ có 7 ký tự                                 | Họ Tên: Nguyen Van A<br>Email: fr20.dt05@test.com<br>Mật khẩu: P@ssw0r<br>Xác nhận mật khẩu: P@ssw0r<br>Bối cảnh: Mobile       | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt05@test.com" vào trường Email.<br>5. Nhập "P@ssw0r" vào trường Mật khẩu.<br>6. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".       | Hiển thị lỗi Mật khẩu phải có tối thiểu 8 ký tự.                        |               |        |           |             |
| FR-20-DT-06  | Từ chối khi Mật khẩu thiếu chữ hoa                                  | Họ Tên: Nguyen Van A<br>Email: fr20.dt06@test.com<br>Mật khẩu: p@ssw0rd<br>Xác nhận mật khẩu: p@ssw0rd<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt06@test.com" vào trường Email.<br>5. Nhập "p@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "p@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ hoa.                        |               |        |           |             |
| FR-20-DT-07  | Từ chối khi Mật khẩu thiếu chữ thường                               | Họ Tên: Nguyen Van A<br>Email: fr20.dt07@test.com<br>Mật khẩu: P@SSW0RD<br>Xác nhận mật khẩu: P@SSW0RD<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt07@test.com" vào trường Email.<br>5. Nhập "P@SSW0RD" vào trường Mật khẩu.<br>6. Nhập "P@SSW0RD" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ thường.                     |               |        |           |             |
| FR-20-DT-08  | Từ chối khi Mật khẩu thiếu chữ số                                   | Họ Tên: Nguyen Van A<br>Email: fr20.dt08@test.com<br>Mật khẩu: P@ssword<br>Xác nhận mật khẩu: P@ssword<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt08@test.com" vào trường Email.<br>5. Nhập "P@ssword" vào trường Mật khẩu.<br>6. Nhập "P@ssword" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ số.                         |               |        |           |             |
| FR-20-DT-09  | Từ chối khi Mật khẩu thiếu ký tự đặc biệt                           | Họ Tên: Nguyen Van A<br>Email: fr20.dt09@test.com<br>Mật khẩu: Password1<br>Xác nhận mật khẩu: Password1<br>Bối cảnh: Mobile   | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt09@test.com" vào trường Email.<br>5. Nhập "Password1" vào trường Mật khẩu.<br>6. Nhập "Password1" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".   | Hiển thị lỗi Mật khẩu phải có ít nhất 1 ký tự đặc biệt hợp lệ.          |               |        |           |             |
| FR-20-DT-10  | Từ chối khi Xác nhận mật khẩu không khớp                            | Họ Tên: Nguyen Van A<br>Email: fr20.dt10@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rD<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.dt10@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rD" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hiển thị lỗi Xác nhận mật khẩu không khớp với Mật khẩu.                 |               |        |           |             |

## Boundary Value Analysis

### Giải thích

Trong FR-20, các ràng buộc có tính chất biên và có thể lượng hóa bằng số hoặc độ dài chuỗi gồm:

1. **Độ dài Mật khẩu**
   - Ràng buộc tối thiểu: 8 ký tự.
   - Điểm biên cần xét: 7 ký tự, 8 ký tự, 9 ký tự.
   - Tại $n = 7$, hệ thống phải từ chối vì nhỏ hơn ngưỡng tối thiểu.
   - Tại $n = 8$, hệ thống phải chấp nhận nếu các điều kiện thành phần khác đều hợp lệ.
   - Tại $n = 9$, hệ thống vẫn phải chấp nhận nếu các điều kiện thành phần khác đều hợp lệ.

2. **Số lượng chữ hoa trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 chữ hoa.
   - Điểm biên cần xét: 0 chữ hoa, 1 chữ hoa, 2 chữ hoa.

3. **Số lượng chữ thường trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 chữ thường.
   - Điểm biên cần xét: 0 chữ thường, 1 chữ thường, 2 chữ thường.

4. **Số lượng chữ số trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 chữ số.
   - Điểm biên cần xét: 0 chữ số, 1 chữ số, 2 chữ số.

5. **Số lượng ký tự đặc biệt trong Mật khẩu**
   - Ràng buộc tối thiểu: ít nhất 1 ký tự đặc biệt thuộc tập `@`, `$`, `!`, `%`, `*`, `?`, `&`.
   - Điểm biên cần xét: 0 ký tự đặc biệt, 1 ký tự đặc biệt, 2 ký tự đặc biệt.

6. **Số lượng trường bắt buộc trên form**
   - Ràng buộc nghiệp vụ: 4 trường bắt buộc phải được nhập đầy đủ.
   - Điểm biên cần xét theo kiểm tra thực thi luồng: 3 trường hợp điền đủ và 1 trường bỏ trống để xác nhận hệ thống ngăn submit.

Từ góc nhìn kiểm thử, các điểm 0, 1 và 2 là vùng nhạy cảm vì lỗi thường phát sinh tại ngưỡng tối thiểu: lập trình viên có thể so sánh sai điều kiện "lớn hơn" với "lớn hơn hoặc bằng", hoặc đếm sai số lượng ký tự ở đúng ngưỡng chuyển trạng thái hợp lệ. Khi kiểm tra biên của một biến, các trường bắt buộc khác trên form phải luôn được điền bằng giá trị hợp lệ để cô lập lỗi.

### Boundary Test Cases

| Test Case ID | Description                                 | Input Data                                                                                                                                        | Test Steps                                                                                                                                                                                                                                                                                                           | Expected Result                                                                                             | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-20-BVA-01 | Kiểm tra Mật khẩu tại biên dưới với 7 ký tự | Họ Tên: Nguyen Van A<br>Email: fr20.bva01@test.com<br>Mật khẩu: P@ssw0r (7 ký tự)<br>Xác nhận mật khẩu: P@ssw0r (7 ký tự)<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.bva01@test.com" vào trường Email.<br>5. Nhập "P@ssw0r" vào trường Mật khẩu.<br>6. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hệ thống từ chối vì độ dài mật khẩu chỉ đạt 7 ký tự, nhỏ hơn ngưỡng tối thiểu 8 ký tự.                      |               |        |           |             |
| FR-20-BVA-02 | Kiểm tra Mật khẩu tại biên với 8 ký tự      | Họ Tên: Nguyen Van A<br>Email: fr20.bva02@test.com<br>Mật khẩu: P@ssw0rd (8 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd (8 ký tự)<br>Bối cảnh: Mobile   | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.bva02@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".   | Hệ thống chấp nhận vì mật khẩu đạt đúng ngưỡng tối thiểu 8 ký tự và thỏa các điều kiện thành phần bắt buộc. |               |        |           |             |
| FR-20-BVA-03 | Kiểm tra Mật khẩu tại biên trên với 9 ký tự | Họ Tên: Nguyen Van A<br>Email: fr20.bva03@test.com<br>Mật khẩu: P@ssw0rd1 (9 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd1 (9 ký tự)<br>Bối cảnh: Mobile | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.bva03@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd1" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd1" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký". | Hệ thống chấp nhận vì mật khẩu vượt qua ngưỡng tối thiểu và vẫn thỏa toàn bộ điều kiện bảo mật.             |               |        |           |             |

## AI Gap Analysis
**Phần này giống với FR-01: Đăng ký tài khoản.**