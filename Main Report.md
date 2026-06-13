# Thông tin chung
- Họ và tên: Lưu Huy Hoàng
- MSSV: 23127047

# FR-01: Đăng ký tài khoản

## Domain Testing

### Giải thích
Để áp dụng kỹ thuật Equivalence Partitioning (Phân hoạch miền tương đương) và Combinatorial Testing (Kiểm thử tổ hợp) cho tính năng đăng ký tài khoản, chúng ta cần phân tích từng biến đầu vào và xác định các miền tương đương hợp lệ và không hợp lệ.

1. **Họ Tên**:
   - Miền hợp lệ: Không rỗng, ví dụ "Nguyễn Văn A".
   - Miền không hợp lệ: Rỗng, ví dụ "".

2. **Email**:
   - Miền hợp lệ: Định dạng hợp lệ và duy nhất, ví dụ "example@gmail.com".
   - Miền không hợp lệ: Không có định dạng hợp lệ hoặc không duy nhất, ví dụ "example" hoặc "example@gmail.com" (nếu đã tồn tại).

3. **Mật khẩu**:
   - Miền hợp lệ: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, và 1 ký tự đặc biệt, ví dụ "P@ssw0rd".
   - Miền không hợp lệ: Không đủ 8 ký tự, hoặc thiếu một trong các yêu cầu (chữ hoa, chữ thường, chữ số, ký tự đặc biệt), ví dụ "password" hoặc "P@ssword".

4. **Xác nhận mật khẩu**:
   - Miền hợp lệ: Phải khớp với trường Mật khẩu, ví dụ nếu Mật khẩu là "P@ssw0rd" thì Xác nhận mật khẩu cũng phải là "P@ssw0rd".
   - Miền không hợp lệ: Không khớp với trường Mật khẩu, ví dụ nếu Mật khẩu là "P@ssw0rd" thì Xác nhận mật khẩu là "P@ssword".

### Bảng Test Cases
| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-01-DT-01 | Đăng ký thành công với thông tin hợp lệ | Họ Tên: Nguyễn Văn A<br>Email: web.fr01.dt01@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "web.fr01.dt01@test.com", điền trường Mật khẩu là "P@ssw0rd", điền trường Xác nhận mật khẩu là "P@ssw0rd".<br>3. Nhấn nút "Đăng ký". | Đăng ký thành công và chuyển tới trang Đăng nhập. |  |  |  |  |
| FR-01-DT-02 | Đăng ký không thành công do Họ Tên rỗng | Họ Tên: <br>Email: example@gmail.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "P@ssw0rd", điền trường Xác nhận mật khẩu là "P@ssw0rd".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Họ Tên rỗng. |  |  |  |  |
| FR-01-DT-03 | Đăng ký không thành công do Email không hợp lệ | Họ Tên: Nguyễn Văn A<br>Email: example<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example", điền trường Mật khẩu là "P@ssw0rd", điền trường Xác nhận mật khẩu là "P@ssw0rd".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Email không hợp lệ. |  |  |  |  |
| FR-01-DT-04 | Đăng ký không thành công do Mật khẩu không đủ 8 ký tự | Họ Tên: Nguyễn Văn A<br>Email: example@gmail.com<br>Mật khẩu: P@ss<br>Xác nhận mật khẩu: P@ss | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "P@ss", điền trường Xác nhận mật khẩu là "P@ss".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Mật khẩu không đủ 8 ký tự. |  |  |  |  |
| FR-01-DT-05 | Đăng ký không thành công do Xác nhận mật khẩu không khớp | Họ Tên: Nguyễn Văn A<br>Email: example@gmail.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssword | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "P@ssw0rd", điền trường Xác nhận mật khẩu là "P@ssword".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Xác nhận mật khẩu không khớp. |  |  |  |  |
| FR-01-DT-06 | Đăng ký không thành công do Email đã tồn tại | Họ Tên: Nguyễn Văn A<br>Email: web.fr01.existing@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "web.fr01.existing@test.com", điền trường Mật khẩu là "P@ssw0rd", điền trường Xác nhận mật khẩu là "P@ssw0rd".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Email đã tồn tại. |  |  |  |  |
| FR-01-DT-07 | Đăng ký không thành công do Mật khẩu thiếu chữ hoa | Họ Tên: Nguyễn Văn A<br>Email: example@gmail.com<br>Mật khẩu: p@ssw0rd<br>Xác nhận mật khẩu: p@ssw0rd | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "p@ssw0rd", điền trường Xác nhận mật khẩu là "p@ssw0rd".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Mật khẩu thiếu chữ hoa. |  |  |  |  |
| FR-01-DT-08 | Đăng ký không thành công do Mật khẩu thiếu chữ thường | Họ Tên: Nguyễn Văn A<br>Email: example@gmail.com<br>Mật khẩu: P@SSW0RD<br>Xác nhận mật khẩu: P@SSW0RD | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "P@SSW0RD", điền trường Xác nhận mật khẩu là "P@SSW0RD".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Mật khẩu thiếu chữ thường. |  |  |  |  |
| FR-01-DT-09 | Đăng ký không thành công do Mật khẩu thiếu chữ số | Họ Tên: Nguyễn Văn A<br>Email: example@gmail.com<br>Mật khẩu: P@ssword<br>Xác nhận mật khẩu: P@ssword | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "P@ssword", điền trường Xác nhận mật khẩu là "P@ssword".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Mật khẩu thiếu chữ số. |  |  |  |  |
| FR-01-DT-10 | Đăng ký không thành công do Mật khẩu thiếu ký tự đặc biệt | Họ Tên: Nguyễn Văn A<br>Email: example@gmail.com<br>Mật khẩu: Password1<br>Xác nhận mật khẩu: Password1 | 1. Truy cập trang đăng ký.<br>2. Điền trường Họ Tên là "Nguyễn Văn A", điền trường Email là "example@gmail.com", điền trường Mật khẩu là "Password1", điền trường Xác nhận mật khẩu là "Password1".<br>3. Nhấn nút "Đăng ký". | Hiển thị lỗi do Mật khẩu thiếu ký tự đặc biệt. |  |  |  |  |

## Boundary Value Analysis
### Giải thích
Để áp dụng kỹ thuật Boundary Value Analysis (BVA) cho quá trình đăng ký tài khoản, chúng ta cần xác định các điểm ranh giới nhạy cảm cho từng biến đầu vào. Dưới đây là phân tích từng bước, chỉ áp dụng cho trường Mật khẩu vì đây là trường có ràng buộc rõ ràng về độ dài và yêu cầu ký tự:

1. **Mật khẩu**: Với ràng buộc tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, và 1 ký tự đặc biệt, các điểm ranh giới sẽ là:
   - Boundary dưới (MIN): 8 ký tự
   - Boundary - 1: 7 ký tự (không hợp lệ)
   - Boundary + 1: 9 ký tự (hợp lệ nếu đáp ứng các yêu cầu khác)


### Bảng Test Cases
| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-01-BVA-01 | Kiểm tra Mật khẩu Boundary - 1 (7 ký tự) | Họ Tên: Nguyen Van A<br>Email: web.fr01.bva.01@test.com<br>Mật khẩu: P@ssw0r<br>Xác nhận mật khẩu: P@ssw0r | 1. Truy cập trang đăng ký.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên, nhập "web.fr01.bva.01@test.com" vào trường Email, nhập "P@ssw0r" vào trường Mật khẩu, nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>3. Click chuột vào nút "Đăng ký" để gửi dữ liệu hệ thống. | Lỗi: Mật khẩu phải có ít nhất 8 ký tự. |  |  |  |  |
| FR-01-BVA-02 | Kiểm tra Mật khẩu Boundary (8 ký tự) | Họ Tên: Nguyen Van A<br>Email: web.fr01.bva.02@test.com<br>Mật khẩu: P@ssw0rd<br>Xác nhận mật khẩu: P@ssw0rd | 1. Truy cập trang đăng ký.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên, nhập "web.fr01.bva.02@test.com" vào trường Email, nhập "P@ssw0rd" vào trường Mật khẩu, nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>3. Click chuột vào nút "Đăng ký" để gửi dữ liệu hệ thống. | Đăng ký thành công, hệ thống chuyển tới trang Đăng nhập. |  |  |  |  |
| FR-01-BVA-03 | Kiểm tra Mật khẩu Boundary + 1 (9 ký tự) | Họ Tên: Nguyen Van A<br>Email: web.fr01.bva.03@test.com<br>Mật khẩu: P@ssw0rd1<br>Xác nhận mật khẩu: P@ssw0rd1 | 1. Truy cập trang đăng ký.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên, nhập "web.fr01.bva.03@test.com" vào trường Email, nhập "P@ssw0rd1" vào trường Mật khẩu, nhập "P@ssw0rd1" vào trường Xác nhận mật khẩu.<br>3. Click chuột vào nút "Đăng ký" để gửi dữ liệu hệ thống. | Đăng ký thành công, hệ thống chuyển tới trang Đăng nhập. |  |  |  |  |


## AI gap analysis
1. AI tự bịa thêm ràng buộc không có trong spec
- Ở phần BVA, AI đã tự đặt ra các giới hạn độ dài cho trường Họ Tên (MIN = 1, MAX = 50) và thậm chí cả độ dài từng phần của Email (trước/sau dấu @) — trong khi spec gốc hoàn toàn không đề cập đến bất kỳ ràng buộc độ dài nào cho hai trường này.
- Đây là hiện tượng AI "tự điền vào chỗ trống" bằng kiến thức chung, thay vì bám sát đúng những gì đặc tả yêu cầu. Trong môi trường kiểm thử thực tế, điều này có thể dẫn đến việc tester tốn công kiểm tra những điều kiện hệ thống chưa bao giờ định nghĩa, hoặc tệ hơn là phát sinh bug report sai lệch so với yêu cầu thực tế.

2. BVA bị dùng sai kỹ thuật ở phần Email
- Trong bảng BVA, AI sinh ra các test case kiểm tra định dạng email hợp lệ/không hợp lệ và email đã tồn tại. Đây là vấn đề về phân loại kỹ thuật.
- BVA về bản chất chỉ có ý nghĩa với các biến có ranh giới số lượng đo đếm được — ví dụ độ dài chuỗi, giá trị số. Định dạng email là ràng buộc cấu trúc logic (có @ hay không, có domain hay không), không phải ranh giới số học, nên nó thuộc về Domain Testing / Equivalence Partitioning — và thực tế đã được cover đầy đủ ở phần DT rồi (FR-01-DT-03, FR-01-DT-06).

3. Hệ quả: Sinh ra test case thừa và trùng lặp
- Hai lỗi trên cộng lại dẫn đến một số test case không có giá trị kiểm thử thực sự:
   - Email hợp lệ
   - Email không hợp lệ
   - Email đã tồn tại
   - Kiểm tra biên độ dài Họ Tên — một ràng buộc AI tự nghĩ ra, không có trong spec

# FR-10: Trạng thái Đơn hàng (Order State Machine)
## Domain Testing
### Giải thích
Để thiết kế bộ kịch bản kiểm thử cho trạng thái đơn hàng, chúng ta cần phân tích từng biến đầu vào và xác định các miền tương đương hợp lệ và không hợp lệ.

1. **Trạng thái hiện tại của đơn hàng (current_state)**: 
   - Miền hợp lệ: `pending`, `confirmed`, `shipping`, `delivered`, `canceled`
   - Miền không hợp lệ: bất kỳ giá trị nào khác ngoài 5 giá trị trên

2. **Hành động được thực hiện (action)**: 
   - Miền hợp lệ: `xác nhận`, `giao hàng`, `hoàn tất`, `hủy`
   - Miền không hợp lệ: bất kỳ giá trị nào khác ngoài 4 giá trị trên

3. **Người thực hiện hành động (actor)**: 
   - Miền hợp lệ: `Admin`, `User`
   - Miền không hợp lệ: bất kỳ giá trị nào khác ngoài 2 giá trị trên

Áp dụng quy tắc "Phủ định từng thành phần" (Single Negative Fault Isolation) cho từng trường dữ liệu có chứa nhiều ràng buộc phức tạp lồng nhau, chúng ta sẽ kiểm tra từng thành phần một cách độc lập.

### Bảng Test Cases
| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-10-DT-01 | Kiểm tra chuyển đổi trạng thái từ `pending` sang `confirmed` bởi `Admin` | current_state: pending<br>action: xác nhận<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Thực hiện hành động `xác nhận` bởi `Admin`. | Trạng thái đơn hàng chuyển thành `confirmed` |  |  |  |  |
| FR-10-DT-02 | Kiểm tra chuyển đổi trạng thái từ `confirmed` sang `shipping` bởi `Admin` | current_state: confirmed<br>action: giao hàng<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Thực hiện hành động `giao hàng` bởi `Admin`. | Trạng thái đơn hàng chuyển thành `shipping` |  |  |  |  |
| FR-10-DT-03 | Kiểm tra chuyển đổi trạng thái từ `shipping` sang `delivered` bởi `Admin` | current_state: shipping<br>action: hoàn tất<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Thực hiện hành động `hoàn tất` bởi `Admin`. | Trạng thái đơn hàng chuyển thành `delivered` |  |  |  |  |
| FR-10-DT-04 | Kiểm tra hủy đơn hàng ở trạng thái `pending` bởi `User` | current_state: pending<br>action: hủy<br>actor: User | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Thực hiện hành động `hủy` bởi `User`. | Trạng thái đơn hàng chuyển thành `canceled` |  |  |  |  |
| FR-10-DT-05 | Kiểm tra chuyển đổi trạng thái không hợp lệ từ `delivered` sang `confirmed` | current_state: delivered<br>action: xác nhận<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `delivered`.<br>3. Thực hiện hành động `xác nhận` bởi `Admin`. | Trả về lỗi với thông báo phù hợp |  |  |  |  |
| FR-10-DT-06 | Kiểm tra chuyển đổi trạng thái không hợp lệ từ `canceled` sang `shipping` | current_state: canceled<br>action: giao hàng<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `canceled`.<br>3. Thực hiện hành động `giao hàng` bởi `Admin`. | Trả về lỗi với thông báo phù hợp |  |  |  |  |
| FR-10-DT-07 | Kiểm tra hành động không hợp lệ bởi `User` | current_state: pending<br>action: xác nhận<br>actor: User | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Thực hiện hành động `xác nhận` bởi `User`. | Trả về lỗi với thông báo phù hợp |  |  |  |  |
| FR-10-DT-08 | Kiểm tra hủy đơn hàng ở trạng thái `shipping` bởi `Admin` | current_state: shipping<br>action: hủy<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Thực hiện hành động `hủy` bởi `Admin`. | Trạng thái đơn hàng chuyển thành `canceled` |  |  |  |  |
| FR-10-DT-09 | Kiểm tra chuyển đổi trạng thái không hợp lệ từ `pending` sang `delivered` | current_state: pending<br>action: hoàn tất<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `pending`.<br>3. Thực hiện hành động `hoàn tất` bởi `Admin`. | Trả về lỗi với thông báo phù hợp |  |  |  |  |
| FR-10-DT-10 | Kiểm tra chuyển đổi trạng thái từ `confirmed` sang `delivered` | current_state: confirmed<br>action: hoàn tất<br>actor: Admin | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Thực hiện hành động `hoàn tất` bởi `Admin`. | Trả về lỗi với thông báo phù hợp |  |  |  |  |
| FR-10-DT-11 | Kiểm tra hủy đơn hàng ở trạng thái `confirmed` bởi `User` | current_state: confirmed<br>action: hủy<br>actor: User | 1. Truy cập trang quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `confirmed`.<br>3. Thực hiện hành động `hủy` bởi `User`. | Trạng thái đơn hàng chuyển thành `canceled` |  |  |  |  |

## Boundary Value Analysis
### Giải thích
Để áp dụng kỹ thuật Boundary Value Analysis (BVA) cho trạng thái đơn hàng và các hành động liên quan, chúng ta cần xác định các điểm ranh giới nhạy cảm (Boundary) cho từng biến đầu vào có thể có giá trị số hoặc độ dài cụ thể. Tuy nhiên, trong trường hợp này, các biến đầu vào như trạng thái đơn hàng, hành động, và người thực hiện hành động đều là chuỗi và có giá trị cố định, không có độ dài hoặc giá trị số cụ thể cần kiểm tra.

Tuy nhiên, chúng ta có thể áp dụng BVA cho các biến có thể có giá trị biên như số lượng hành động có thể thực hiện, số lượng trạng thái đơn hàng, v.v. Nhưng trong trường hợp này, các giá trị này đều được định nghĩa rõ ràng và không có độ dài hoặc giá trị số cần kiểm tra.

Chúng ta sẽ tập trung vào việc kiểm tra các quy tắc nghiệp vụ và logic ngầm quan trọng đã được định nghĩa. Mỗi quy tắc sẽ được kiểm tra với các trường hợp biên khác nhau để đảm bảo rằng hệ thống hoạt động đúng như mong đợi.

### Bảng Test Cases
Kỹ thuật Boundary Value Analysis không áp dụng được cho tính năng FR-10 vì toàn bộ biến đầu vào (current_state, action, actor) đều là tập giá trị enum cố định, không có ranh giới số học hay độ dài chuỗi nào cần kiểm tra tại biên. Các kịch bản chuyển đổi trạng thái hợp lệ/không hợp lệ đã được cover đầy đủ bởi Domain Testing ở trên

## AI gap analysis
1. Domain Testing — Test cases trùng lặp logic
- Phần giải trình Domain Testing bám spec tốt, phân tích đủ 3 biến current_state, action, actor và áp dụng đúng nguyên tắc Single Negative Fault Isolation. Tuy nhiên trong bảng test cases có 2 cặp trùng lặp logic: FR-01-DT-07 (pending + xác nhận + User → Lỗi) trùng hoàn toàn với
FR-01-DT-09 đã được loại bỏ. Bộ còn lại 11 cases đủ coverage.

2. BVA — Toàn bộ test cases bị đặt sai kỹ thuật
- Phần giải trình BVA đã tự nhận thức đúng vấn đề — AI thừa nhận rằng các biến đầu vào của tính năng này đều là chuỗi enum cố định, không có ranh giới số học nào để đo. Đây là điểm hiếm gặp khi AI tự đánh giá đúng giới hạn của mình.
- Tuy nhiên phần kết luận lại mâu thuẫn — thay vì dừng lại, AI vẫn cố sinh ra 9 test cases cho BVA bằng cách kiểm tra các chuyển đổi trạng thái hợp lệ/không hợp lệ. Đây là Domain Testing thuần túy, không liên quan gì đến BVA.
- Về bản chất, tính năng Order State Machine không có thuộc tính nào có đơn vị đo — không có độ dài chuỗi, không có giá trị số, không có ngưỡng thời gian — nên BVA không áp dụng được cho feature này. Đây không phải lỗi của AI mà là đặc thù của bài toán.
