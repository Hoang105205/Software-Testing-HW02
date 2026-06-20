# Thông tin chung
- Họ và tên: Lưu Huy Hoàng
- MSSV: 23127047

# FR-01: Đăng ký tài khoản

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

| Test Case ID | Description                                      | Input Data                                                                                                 | Test Steps                                                                                                                                                                                                                                                       | Expected Result                                                         | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-01-DT-01  | Đăng ký thành công với toàn bộ dữ liệu hợp lệ    | Họ Tên: Nguyen Van A<br>Email: fr01.dt01@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt01@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Đăng ký thành công và hệ thống chuyển sang trang Đăng nhập.             |               |        |           |             |
| FR-01-DT-02  | Từ chối khi Họ Tên bị bỏ trống                   | Họ Tên: <br>Email: fr01.dt02@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd                 | 1. Truy cập trang Đăng ký tài khoản.<br>2. Để trống trường Họ Tên.<br>3. Nhập "fr01.dt02@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".                    | Hiển thị lỗi bắt buộc nhập Họ Tên và không cho phép gửi form.           |               |        |           |             |
| FR-01-DT-03  | Từ chối khi Email sai định dạng do thiếu ký tự @ | Họ Tên: Nguyen Van A<br>Email: fr01.dt03.test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt03.test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hiển thị lỗi định dạng Email không hợp lệ và không cho phép gửi form.   |               |        |           |             |
| FR-01-DT-04  | Từ chối khi Email đã tồn tại trong hệ thống      | Họ Tên: Nguyen Van A<br>Email: fr01.existing@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.existing@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hiển thị lỗi Email đã được sử dụng và không cho phép tạo tài khoản mới. |               |        |           |             |
| FR-01-DT-05  | Từ chối khi Mật khẩu chỉ có 7 ký tự              | Họ Tên: Nguyen Van A<br>Email: fr01.dt05@test.com<br>Mật khẩu: P@ssw0r<br>Xác nhận mật khẩu: P@ssw0r       | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt05@test.com" vào trường Email.<br>4. Nhập "P@ssw0r" vào trường Mật khẩu.<br>5. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".       | Hiển thị lỗi Mật khẩu phải có tối thiểu 8 ký tự.                        |               |        |           |             |
| FR-01-DT-06  | Từ chối khi Mật khẩu thiếu chữ hoa               | Họ Tên: Nguyen Van A<br>Email: fr01.dt06@test.com<br>Mật khẩu: p@ssw0rd<br>Xác nhận mật khẩu: p@ssw0rd     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt06@test.com" vào trường Email.<br>4. Nhập "p@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "p@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ hoa.                        |               |        |           |             |
| FR-01-DT-07  | Từ chối khi Mật khẩu thiếu chữ thường            | Họ Tên: Nguyen Van A<br>Email: fr01.dt07@test.com<br>Mật khẩu: P@SSW0RD<br>Xác nhận mật khẩu: P@SSW0RD     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt07@test.com" vào trường Email.<br>4. Nhập "P@SSW0RD" vào trường Mật khẩu.<br>5. Nhập "P@SSW0RD" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ thường.                     |               |        |           |             |
| FR-01-DT-08  | Từ chối khi Mật khẩu thiếu chữ số                | Họ Tên: Nguyen Van A<br>Email: fr01.dt08@test.com<br>Mật khẩu: P@ssword<br>Xác nhận mật khẩu: P@ssword     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt08@test.com" vào trường Email.<br>4. Nhập "P@ssword" vào trường Mật khẩu.<br>5. Nhập "P@ssword" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hiển thị lỗi Mật khẩu phải có ít nhất 1 chữ số.                         |               |        |           |             |
| FR-01-DT-09  | Từ chối khi Mật khẩu thiếu ký tự đặc biệt        | Họ Tên: Nguyen Van A<br>Email: fr01.dt09@test.com<br>Mật khẩu: Password1<br>Xác nhận mật khẩu: Password1   | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt09@test.com" vào trường Email.<br>4. Nhập "Password1" vào trường Mật khẩu.<br>5. Nhập "Password1" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hiển thị lỗi Mật khẩu phải có ít nhất 1 ký tự đặc biệt hợp lệ.          |               |        |           |             |
| FR-01-DT-10  | Từ chối khi Xác nhận mật khẩu không khớp         | Họ Tên: Nguyen Van A<br>Email: fr01.dt10@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rD     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.dt10@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rD" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hiển thị lỗi Xác nhận mật khẩu không khớp với Mật khẩu.                 |               |        |           |             |

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

| Test Case ID | Description                                 | Input Data                                                                                                                                    | Test Steps                                                                                                                                                                                                                                                      | Expected Result                                                                                             | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-01-BVA-01 | Kiểm tra Mật khẩu tại biên dưới với 7 ký tự | Họ Tên: Nguyen Van A<br>Email: fr01.bva01@test.com<br>Mật khẩu: P@ssw0r (7 ký tự)<br>Xác nhận mật khẩu: P@ssw0r (7 ký tự)                     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva01@test.com" vào trường Email.<br>4. Nhập "P@ssw0r" vào trường Mật khẩu.<br>5. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hệ thống từ chối vì độ dài mật khẩu chỉ đạt 7 ký tự, nhỏ hơn ngưỡng tối thiểu 8 ký tự.                      |               |        |           |             |
| FR-01-BVA-02 | Kiểm tra Mật khẩu tại biên với 8 ký tự      | Họ Tên: Nguyen Van A<br>Email: fr01.bva02@test.com<br>Mật khẩu: P@ssw0rd (8 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd (8 ký tự)                   | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva02@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hệ thống chấp nhận vì mật khẩu đạt đúng ngưỡng tối thiểu 8 ký tự và thỏa các điều kiện thành phần bắt buộc. |               |        |           |             |
| FR-01-BVA-03 | Kiểm tra Mật khẩu tại biên trên với 9 ký tự | Họ Tên: Nguyen Van A<br>Email: fr01.bva03@test.com<br>Mật khẩu: P@ssw0rd1 (9 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd1 (9 ký tự)                 | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva03@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd1" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd1" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hệ thống chấp nhận vì mật khẩu vượt qua ngưỡng tối thiểu và vẫn thỏa toàn bộ điều kiện bảo mật.             |               |        |           |             |


## AI Gap Analysis
1. BVA-04 đến BVA-07 trùng lặp với DT-06 đến DT-09
- Bốn test case BVA-04, BVA-05, BVA-06, BVA-07 có input data và expected result trùng hoàn toàn với DT-06, DT-07, DT-08, DT-09:

    - FR-01-BVA-04 (0 chữ hoa) ← trùng FR-01-DT-06
    - FR-01-BVA-05 (0 chữ thường) ← trùng FR-01-DT-07
    - FR-01-BVA-06 (0 chữ số) ← trùng FR-01-DT-08
    - FR-01-BVA-07 (0 ký tự đặc biệt) ← trùng FR-01-DT-09

- Về bản chất, kiểm tra "0 chữ hoa/thường/số/đặc biệt" là phân hoạch miền không hợp lệ (Invalid Partition) — thuộc Domain Testing, không phải BVA. AI đã xếp nhầm chúng vào BVA để đủ số lượng tối thiểu 6-9 cases theo yêu cầu trong prompt (do prompt lúc chạy Function này của em chưa đủ tối ưu), thay vì chỉ giữ 3 case biên độ dài mật khẩu thực sự thuộc BVA.

# FR-10: Trạng thái Đơn hàng (Order State Machine)
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
| Test Case ID | Description                                | Input Data                                                    | Test Steps                                                                                                                                                           | Expected Result                                                                    | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-10-DT-01  | Xác nhận đơn hàng từ `pending` bởi `Admin` | current_state: pending<br>action: xác nhận<br>actor: Admin    | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Chọn hành động `xác nhận`.<br>4. Thực thi thao tác với vai trò `Admin`.    | Đơn hàng chuyển từ `pending` sang `confirmed`.                                     |               |        |           |             |
| FR-10-DT-02  | Giao hàng đơn từ `confirmed` bởi `Admin`   | current_state: confirmed<br>action: giao hàng<br>actor: Admin | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Chọn hành động `giao hàng`.<br>4. Thực thi thao tác với vai trò `Admin`. | Đơn hàng chuyển từ `confirmed` sang `shipping`.                                    |               |        |           |             |
| FR-10-DT-03  | Hoàn tất đơn từ `shipping` bởi `Admin`     | current_state: shipping<br>action: hoàn tất<br>actor: Admin   | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hoàn tất`.<br>4. Thực thi thao tác với vai trò `Admin`.   | Đơn hàng chuyển từ `shipping` sang `delivered`.                                    |               |        |           |             |
| FR-10-DT-04  | Hủy đơn từ `pending` bởi `User`            | current_state: pending<br>action: hủy<br>actor: User          | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `User`.          | Đơn hàng chuyển từ `pending` sang `canceled`.                                      |               |        |           |             |
| FR-10-DT-05  | Hủy đơn từ `pending` bởi `Admin`           | current_state: pending<br>action: hủy<br>actor: Admin         | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`.         | Đơn hàng chuyển từ `pending` sang `canceled`.                                      |               |        |           |             |
| FR-10-DT-06  | Hủy đơn từ `confirmed` bởi `User`          | current_state: confirmed<br>action: hủy<br>actor: User        | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `User`.        | Đơn hàng chuyển từ `confirmed` sang `canceled`.                                    |               |        |           |             |
| FR-10-DT-07  | Hủy đơn từ `confirmed` bởi `Admin`         | current_state: confirmed<br>action: hủy<br>actor: Admin       | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`.       | Đơn hàng chuyển từ `confirmed` sang `canceled`.                                    |               |        |           |             |
| FR-10-DT-08  | User cố hủy đơn ở trạng thái `shipping`    | current_state: shipping<br>action: hủy<br>actor: User         | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `User`.         | Trả về lỗi, không cho phép `User` tự hủy đơn ở trạng thái `shipping`.              |               |        |           |             |
| FR-10-DT-09  | Admin cố hủy đơn ở trạng thái `shipping`   | current_state: shipping<br>action: hủy<br>actor: Admin        | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`.        | Đơn hàng chuyển từ `shipping` sang `canceled`. |               |        |           |             |
| FR-10-DT-10  | Cố xác nhận đơn đã `delivered`             | current_state: delivered<br>action: xác nhận<br>actor: Admin  | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `delivered`.<br>3. Chọn hành động `xác nhận`.<br>4. Thực thi thao tác với vai trò `Admin`.  | Trả về lỗi vì `delivered` là trạng thái kết thúc, không được chuyển tiếp.          |               |        |           |             |
| FR-10-DT-11  | Cố giao hàng đơn đã `canceled`             | current_state: canceled<br>action: giao hàng<br>actor: Admin  | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `canceled`.<br>3. Chọn hành động `giao hàng`.<br>4. Thực thi thao tác với vai trò `Admin`.  | Trả về lỗi vì `canceled` là trạng thái kết thúc, không được chuyển tiếp.           |               |        |           |             |

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