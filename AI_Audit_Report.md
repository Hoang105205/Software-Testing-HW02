# AI AUDIT REPORT

## Entry 1

### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-08 16:35:12

### Prompt
```text
domain testing và BVA analyst khác gì nhau
tôi tưởng BVA là cái hỗ trợ cho domain testing mà

Hay 2 cái đó sinh ra 2 bộ test case khác nhau
```

### The AI output
```text
Bản chất tư duy của bạn rất chính xác: BVA (Boundary Value Analysis) không thể đứng độc lập mà là kỹ thuật bổ trợ trực tiếp, nâng cao cho Domain Testing. Tuy nhiên, trong thực tế và trong các bài tập lớn, chúng được tách thành 2 bộ test cases hoặc 2 góc nhìn phân tích riêng biệt để tránh bỏ sót lỗi:

Domain Testing (Phân hoạch miền tương đương):

Mục tiêu: Chia không gian dữ liệu thành các nhóm (miền) Hợp lệ và Không hợp lệ dựa trên logic nghiệp vụ.

Cách chọn data: Chọn một giá trị bất kỳ nằm phía trong (vùng an toàn) của miền để đại diện kiểm thử.

Ví dụ (Username độ dài 6-20): Test độ dài bằng 10.

Boundary Value Analysis (Phân tích giá trị biên):

Mục tiêu: Tập trung đào sâu vào ranh giới chuyển giao giữa các miền dữ liệu nhằm tìm lỗi sai dấu toán học (ví dụ viết nhầm ">" thành ">=") hoặc lỗi off-by-one của lập trình viên.

Cách chọn data: Chọn các giá trị sát sườn đường ranh giới (Boundary - 1, Boundary, Boundary + 1).

Ví dụ (Username độ dài 6-20): Test chính xác các độ dài bằng 5, 6, 7 và 19, 20, 21.

Kết luận: Chúng sinh ra hai bộ kịch bản bổ trợ cho nhau. Bạn làm Domain Testing để dựng khung các miền dữ liệu trước, sau đó dùng BVA đặt lên các cạnh biên để nhặt ra các điểm nhạy cảm nhất.
```

---

## Entry 2
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-08 16:44:20

### Prompt
```text
Hiện tại tôi thấy các câu prompt này chưa đủ tốt. Cụ thể: Có thể thấy rằng nó thiếu input data cụ thể, chỉ là "Mật khẩu: 7 ký tự". Thì không biết nó có đúng hay không hay bản chất test case BVA phải vậy ? Tôi nghĩ nó phải là data cụ thể luôn. Ngoài ra Email và Xác nhận mật khẩu không phải là các biến số học để bắt lỗi biên BVA. Hãy cải thiện câu prompt của Agent 2 và Agent 3.
```

### The AI output
```text
Để giải quyết lỗi AI sinh dữ liệu chung chung định tính và bắt sai kỹ thuật biên cho biến logic (Email), chúng ta cần tái cấu trúc chặt chẽ System Prompt của Agent 2 và Agent 3:

AGENT_2_SYSTEM (Domain Testing): Ép bổ sung điều kiện bắt buộc: "Trong ô [Input Data]: BẮT BUỘC phải cung cấp một bộ dữ liệu ĐẦY ĐỦ các trường trên form để test case có thể thực thi độc lập (Full Data Payload). Mỗi trường dữ liệu phải được viết trên một dòng riêng biệt và cách nhau bằng thẻ


".

AGENT_3_SYSTEM (BVA): Định nghĩa lại phạm vi ranh giới và bổ sung quy tắc cô lập biến: "BVA chỉ áp dụng cho các biến có ranh giới số lượng hoặc độ dài số học. Quy tắc cô lập biến (Variable Isolation): Khi kiểm thử biên của một biến (ví dụ: biến Password), toàn bộ các trường dữ liệu bắt buộc khác trên form BẮT BUỘC phải được điền đầy đủ bằng các giá trị HỢP LỆ nhằm đảm bảo hệ thống không bị lỗi ở các trường khác."

Việc phân rã rõ ràng này giúp AI kích hoạt đúng vùng kiến thức chuyên ngành, tạo ra kịch bản chạy thử chuẩn xác và thực thi được ngay trên môi trường hệ thống thật.
```

## Entry 3
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-08 16:58:35

### Prompt
```text
Sửa lỗi kết nối mô hình qua tầng LiteLLM trung gian của CrewAI:
litellm.exceptions.BadRequestError: GroqException - {"error":{"message":"'messages.0' : for 'role:system' the following must be satisfied[('messages.0' : property 'cache_breakpoint' is unsupported)]","type":"invalid_request_error"}}
```

### The AI output
```text
Nguyên nhân lỗi:
Các phiên bản mới của CrewAI mặc định kích hoạt tính năng tự động tạo bộ đệm (Prompt Caching) của LiteLLM bằng cách chèn cờ cache_breakpoint vào tin nhắn hệ thống (role: system). Tuy nhiên, hạ tầng API của nhà cung cấp Groq hiện tại chưa hỗ trợ thuộc tính này, dẫn đến việc gói tin bị từ chối với mã lỗi BadRequestError.

Giải pháp khắc phục triệt để:
Thay vì sử dụng lớp bọc LLM mặc định của CrewAI (vốn bị phụ thuộc vào luồng sinh payload tự động của LiteLLM), chúng ta thực hiện cấu hình trực tiếp cổng kết nối chuẩn của LangChain dành riêng cho Groq là ChatGroq từ thư viện langchain-groq.

Cập nhật mã nguồn tại STEP 1 trong file agent_skill.py:
from langchain_groq import ChatGroq

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

# Khởi tạo mô hình trực tiếp qua ChatGroq để loại bỏ hoàn toàn LiteLLM khỏi luồng payload
groq_llm = ChatGroq(
    model=GROQ_MODEL,
    temperature=0.2
)

Biện pháp chuyển đổi tầng driver kết nối này giúp dọn sạch các thuộc tính thừa trong gói JSON gửi đi, giúp script kết nối thông suốt với Groq và kích hoạt Agent chạy mượt mà.
```

## Entry 4
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-08 17:22:10

### Prompt
```text
Nói chung về định dạng này kìa ổn rồi. Nhưng tôi muốn cải thiện thêm chút nữa, tôi đánh giá rằng số lượng test case cũng như mục đích các test cases chưa cover được hết. Do đó hãy cải thiện câu prompt của agent 2 và 3 cho tốt hơn (Giải quyết vấn đề Agent lười biếng sinh thiếu trường hợp test của mật khẩu và bỏ quên lỗi biên trường họ tên).
```

### The AI output
```text
Để giải quyết triệt để sự "lười biếng" cố hữu của các mô hình LLM lớn, chúng ta cần đưa vào System Prompt hai kỹ thuật điều phối nâng cao bao gồm: Thiết lập hạn mức số lượng kịch bản tối thiểu và Nguyên tắc phân rã lỗi độc lập (Equivalence Boundary Isolation).

Cải tiến cấu trúc Prompt chi tiết:

Nâng cấp AGENT_2_SYSTEM (Domain Testing):

Chèn thêm luật cứng (ANTI-LAZINESS RULES): "Số lượng kịch bản tối thiểu: Bắt buộc phải sinh ra ít nhất từ 8 đến 12 test cases trở lên".

Ép quy tắc phân rã: Đối với các trường có nhiều ràng buộc phức tạp như Mật khẩu, không được gom chung một ca test lỗi chung chung. Phải tách riêng biệt thành các ca test độc lập: Mật khẩu hợp lệ nhưng thiếu chữ hoa; thiếu chữ thường; thiếu chữ số; thiếu ký tự đặc biệt; chỉ chứa toàn ký tự đặc biệt.

Nâng cấp AGENT_3_SYSTEM (BVA):

Chèn thêm luật cứng: "Số lượng kịch bản tối thiểu: Bắt buộc phải sinh ra ít nhất từ 6 đến 9 test cases biên trở lên".

Áp dụng tư duy Đa biên (Multi-variable Boundaries): Phải quét qua tất cả các biến có tính chất biên độ dài chuỗi xuất hiện trong đặc tả (Ví dụ: Nếu cả trường Họ Tên, Username, hay Mật khẩu đều có ràng buộc độ dài, bạn phải thực hiện tìm các điểm nhạy cảm Boundary-1, Boundary, Boundary+1 cho TỪNG trường đó, không được chỉ làm mỗi trường Mật khẩu).

Bộ prompt nâng cấp này ép Agent phải phân rã triệt để không gian kịch bản đầu vào, giúp gia tăng đáng kể độ bao phủ kiểm thử (Test Coverage) cho hệ thống.
```

## Entry 5
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-09 15:45:22

### Prompt
```text
Trích xuất nghiên cứu từ tài liệu AI:
"Agent Skill" trong giới IT hiện tại không có một định nghĩa chuẩn duy nhất — nó được dùng theo 2 nghĩa tùy context:
Nghĩa 1 — Capability của một AI Agent (Đóng gói một Tool/Function cụ thể).
Nghĩa 2 — Reusable Workflow (Hướng Anthropic/agentskills.io - Đóng gói Instruction mô tả cách hoàn thành một loại task cụ thể).

Theo bạn file tôi đang làm có được gọi là "agent skill" hay không? Hay như thế nào mới là đúng. Tôi có nên chuyển sang viết lệnh vào file markdown không? Nếu dùng cách đó thì cách dùng là gì?
```

### The AI output
```text
Bản chất tệp tin agent_skill.py hiện tại của bạn đóng vai trò là một "Multi-Agent Orchestration Workflow" (Luồng điều phối tuần tự đa Agent) chứ không phải là một "Agent Skill" đơn lẻ. Bạn đang chủ động hard-code luồng dữ liệu đi từ Agent 1 sang Agent 2 và Agent 3 một cách tuyến tính.

Để đúng bản chất kỹ thuật:
1. "Agent Skill" đúng nghĩa phải là một năng lực hoặc một hành động độc lập (ví dụ: một Prompt chuyên biệt hay một Function gọi API), được con Agent chính tự do lựa chọn và kích hoạt khi cần thiết (tư duy ReAct). Các khối Prompt cấu hình kiểm thử (Domain Testing, BVA) thực chất chính là các "Skills" chuyên môn của hệ thống.
2. Việc chuyển đổi câu lệnh (Prompt) sang tệp tin Markdown là một pattern thiết kế AI nâng cao (Prompt-as-a-Service / Instruction-based Skill File). Cách dùng trong thực tế là tệp Python đóng vai trò làm Engine trung tâm, sử dụng các hàm đọc tệp (File I/O) để nạp động nội dung từ các file Markdown này vào cấu trúc system_prompt tại thời điểm gọi API. 

Mô hình tách biệt này giúp mã nguồn Python vô cùng sạch sẽ, đồng thời cho phép người dùng tối ưu chỉ thị kiểm thử trong file Markdown hàng ngày mà không cần can thiệp vào logic code của hệ thống, giảm thiểu tối đa rủi ro phát sinh lỗi cú pháp lập trình.
```

## Entry 6
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-09 15:52:10

### Prompt
```text
Tách ra về cấu trúc nó chỉ như là refactor thôi mà. Tôi đang muốn hỏi về việc thế nào là "agent skill", và cách triển khai nó chuẩn thực tế ngoài doanh nghiệp.
```

### The AI output
```text
Đánh giá của bạn hoàn toàn chính xác, việc chuyển prompt ra file markdown thuần túy mới dừng lại ở bước Refactor mã nguồn (Tách biệt mã nguồn và cấu hình). Trong kiến trúc phần mềm thực tế, "Agent Skill" được định nghĩa và triển khai theo 2 mô hình chuẩn công nghiệp sau:

Mô hình 1: Đóng gói Skill thành các Công cụ lập trình (Tool / Function Calling)
Định nghĩa Skill như một hàm lập trình độc lập có kèm mô tả (Description) tường minh về chức năng, tham số đầu vào và kết quả đầu ra để LLM tự nhận diện.
- Triển khai: Đăng ký các hàm này vào danh mục công cụ (toolbox) của Agent (ví dụ: agent.tools = [domain_testing_skill, bva_skill]). 
- Vận hành: Agent sử dụng vòng lặp tư duy ReAct (Reasoning + Acting) để tự ra quyết định ngầm trong chuỗi suy nghĩ (Chain-of-Thought) xem khi nào cần gọi Skill nào nhằm giải quyết bài toán, lập trình viên không cần can thiệp sắp đặt luồng chạy tuyến tính.

Mô hình 2: Đóng gói Skill thành các Tệp tin Instruction độc lập (Prompt-as-a-Skill)
Đây là hướng tiếp cận theo Open Standard (tiêu chuẩn mở như agentskills.io). Khi đó, mỗi "Skill" được xem là một gói năng lực nghiệp vụ, tách rời hoàn toàn khỏi Logic Core của hệ thống.
- Cấu trúc thư mục chuẩn thực tế:
  EShop_QA_Agent/
  ├── core_engine.py       # Chỉ làm nhiệm vụ kết nối API, điều phối chung
  └── agent_skills/        # Thư mục chứa các Skill độc lập
      ├── spec_analyst.md  # Skill bóc tách của BA
      ├── domain_expert.md # Skill phân rã miền của QA
      └── bva_expert.md    # Skill quét giá trị biên của QA
- Vận hành: Khi core_engine khởi động, nó quét thư mục agent_skills/ để nạp động các tệp tin này vào bộ nhớ. Hệ thống tự động ánh xạ (Mapping) xem Skill nào phù hợp để đưa vào cấu trúc system_prompt của lượt gọi API đó dựa trên ngữ cảnh tác vụ, đem lại tính linh hoạt và khả năng mở rộng tối đa cho hệ thống.
```

## Entry 7
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-10 11:30:15

### Prompt
```text
Trong đề bài có yêu cầu "Provide a detailed, step-by-step explanation of how you applied the technique." nhưng kết quả của AI đôi khi có đôi khi không. Do đó tôi đã thêm dòng "Cách bạn tư duy và" vào mục số 1 của Agent 2 và Agent 3. Theo bạn đánh giá thì 2 câu prompt này của tôi ổn chưa hay bạn có optimize gì thêm không?
```

### The AI output
```text
Việc chèn thêm cụm từ "Cách bạn tư duy và" là một kỹ thuật Prompt Engineering rất tốt giúp kích hoạt chuỗi suy luận Chain-of-Thought (CoT) của mô hình. Tuy nhiên, LLM vẫn có xu hướng làm tắt hoặc bỏ quên lý thuyết khi phải tập trung sinh bảng Markdown quá dài (hiện tượng Lost in the Middle).

Để tối ưu hóa tuyệt đối và đảm bảo không bao giờ bị rơi rụng phần giải trình, chúng ta cần bổ sung kỹ thuật cưỡng chế bố cục đầu ra (Output Formatting Anchor) bằng cách ép cứng các tiêu đề Heading ở cuối Prompt cho Agent 2 và Agent 3:

1. Đối với agent_2_domain_testing.md, chèn thêm đoạn neo bố cục:
BẮT BUỘC ĐỊNH DẠNG ĐẦU RA THEO CẤU TRÚC HEADING SAU:
### I. DETAILED STEP-BY-STEP DOMAIN ANALYSIS
### II. DOMAIN TEST CASES TABLE

2. Đối với agent_3_bva.md, chèn thêm đoạn neo bố cục:
BẮT BUỘC ĐỊNH DẠNG ĐẦU RA THEO CẤU TRÚC HEADING SAU:
### I. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS
### II. BOUNDARY TEST CASES TABLE

Việc ép cấu trúc này buộc AI phải hoàn thành việc điền nội dung giải trình tư duy khoa học vào mục I trước khi được phép vẽ bảng kịch bản ở mục II, đáp ứng trọn vẹn barem điểm của đề bài.
```

## Entry 8
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-10 11:38:12

### Prompt
```text
Mục chiến lược phân rã lỗi của mật khẩu (thiếu chữ hoa, chữ thường, số, ký tự đặc biệt) trong Prompt của Agent 2 và Agent 3 hiện tại có bị coi là quá hard-code không? Vì nó chỉ phù hợp cho đúng 1 chức năng đăng ký tài khoản, còn nếu đưa những đặc tả của chức năng khác vào hệ thống thì xử lý thế nào?
```

### The AI output
```text
Nhận định của bạn hoàn toàn chính xác. Việc đưa các ví dụ cụ thể về mật khẩu vào file kỹ năng tổng quát sẽ làm mất đi tính tái sử dụng (Reusability) của một Agent Skill thực thụ khi đối mặt với các biểu mẫu khác (như form thanh toán thẻ, form tìm kiếm).

Để trừu tượng hóa (Abstract) năng lực này thành luật tư duy tổng quát cho mọi loại biểu mẫu, chúng ta cần refactor lại cấu trúc Prompt như sau:

1. Thay thế luật mật khẩu cụ thể trong Agent 2 bằng "Chiến lược Phân rã ràng buộc" (Constraint Decomposition Strategy):
"Đối với bất kỳ trường dữ liệu nào có chứa nhiều ràng buộc phức tạp lồng nhau (Ví dụ: Định dạng chuỗi, Quy tắc logic, Tập ký tự bắt buộc), bạn KHÔNG được gộp chung các lỗi vào một ca test. Phải áp dụng tư duy 'Phủ định từng thành phần' (Single Negative Fault Isolation): Thiết kế riêng biệt các kịch bản lỗi, trong đó giữ toàn bộ các ràng buộc khác ở trạng thái HỢP LỆ và chỉ làm VI PHẠM duy nhất một ràng buộc cụ thể."

2. Thay thế luật mật khẩu trong Agent 3 bằng "Tư duy Đa biên" (Multi-variable Boundaries):
"Phải tự động quét qua và xác định tất cả các biến có tính chất biên số học hoặc độ dài xuất hiện trong đặc tả (Ví dụ: Biên độ dài Họ Tên, biên số lượng sản phẩm, biên khoảng giá tiền, biên ký tự mật khẩu...). Bạn phải thực hiện tìm các điểm nhạy cảm Boundary-1, Boundary, Boundary+1 cho TỪNG trường hợp đó để tránh bỏ sót."

Sự thay đổi này giúp bộ kỹ năng của Multi-Agent trở nên linh hoạt 100%, sẵn sàng xử lý chính xác bất kỳ tệp đặc tả chức năng nào được nạp vào pipeline.
```

## Entry 9
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-10 11:40:05

### Prompt
```text
Có một vấn đề phát sinh là khi luồng chạy đến Agent cuối cùng (Agent 4 - Report Writer), nó lại tự ý dọn dẹp, tổng hợp và làm gọn mất nội dung giải trình chi tiết hoặc cắt xén bớt số lượng test cases của các Agent trước. Làm sao để giải quyết?
```

### The AI output
```text
Hành vi này xuất hiện do LLM mặc định gán cho vai trò "Technical Writer" xu hướng biên tập ngắn gọn, súc tích. Để kiểm soát và tước bỏ quyền tự ý sáng tạo/rút gọn của Agent 4, chúng ta cần nâng cấp tệp cấu hình bằng kỹ thuật Cưỡng chế giữ nguyên khối (Strict Injection & No-Omission Enforcement).

Nội dung Prompt nâng cấp cho file agent_4_report_writer.md:
"Nhiệm vụ tối cao của bạn là tiếp nhận kết quả thô từ các Agent trước và ghép nối chúng thành một file báo cáo Markdown duy nhất theo đúng cấu trúc hệ thống, TUYỆT ĐỐI KHÔNG ĐƯỢC TỰ Ý BIÊN TẬP HOẶC TÓM TẮT LẠI NỘI DUNG.
QUY TẮC CƯỠNG CHẾ GIỮ NGUYÊN VẸN (STRICT NO-OMISSION RULES):
1. GIỮ NGUYÊN 100% NỘI DUNG: Không được phép tóm tắt, rút gọn, lược bỏ hoặc làm mờ bất kỳ dòng giải trình lý thuyết nào của Agent 2 và Agent 3.
2. KHÔNG ĐƯỢC THU GỌN BẢNG TEST CASES: Bản danh sách Test Cases của cả hai kỹ thuật nhả ra có bao nhiêu dòng thì phải sao chép chính xác toàn bộ bấy nhiêu dòng vào báo cáo cuối cùng. Nghiêm cấm hành vi sử dụng dấu ba chấm (...) hoặc gộp các ca test lại làm một.
3. BẢO TOÀN THẺ ĐỊNH DẠNG: Giữ nguyên vẹn toàn bộ các thẻ <br> dùng để ngắt dòng trong tất cả các ô [Input Data] và [Test Steps]."

Biện pháp đặt ra tối hậu thư này biến Agent 4 thành một bộ ráp nối cơ học thuần túy, bảo toàn tuyệt đối độ bao phủ và nội dung kỹ thuật từ các Agent chuyên môn phía trước.
```

## Entry 10
### AI tool name
* Gemini (Adaptive AI Collaborator)

### Date and time
* 2026-06-10 11:41:25

### Prompt
```text
Ở phần cột Test Steps trong bảng kết quả trả về hiện tại đang bị thiếu thông tin thao tác cụ thể, chỉ ghi chung chung là "Nhập thông tin đăng ký" hoặc "Submit form". Trong khi tôi muốn ghi rõ chi tiết Bước 1 điền cái gì, Bước 2 điền cái gì bám sát dữ liệu thực tế. Hãy tối ưu Prompt cho các Agent.
```

### The AI output
```text
Để loại bỏ tình trạng Agent sinh các bước thực hiện mang tính định tính mơ hồ, chúng ta cần nhúng quy tắc "Kịch bản hóa hành vi nhập liệu" (Behavioral Data Mapping) trực tiếp vào chỉ thị của Agent thiết kế (Agent 2, Agent 3) và Agent tổng hợp (Agent 4):

1. Cập nhật chỉ thị trong ô [Test Steps] cho Agent 2 (Domain) và Agent 3 (BVA):
"QUY TẮC CỘT TEST STEPS (BẮT BUỘC): KHÔNG ĐƯỢC ghi chung chung kiểu 'Nhập thông tin form'. Bạn phải viết chi tiết hành vi tương tác với giao diện theo từng bước, chỉ rõ trường nào nhận giá trị nào từ cột Input Data và phân tách bằng thẻ <br>.
* Ví dụ chuẩn định dạng: 1. Truy cập trang đăng ký.<br>2. Nhập chuỗi [Giá trị họ tên] vào trường Họ Tên, nhập [Giá trị email] vào trường Email, nhập chuỗi [Giá trị mật khẩu] vào trường Mật khẩu, nhập [Giá trị xác nhận mật khẩu] vào trường Xác nhận mật khẩu.<br>3. Click chuột vào nút 'Đăng ký' để gửi dữ liệu hệ thống."

2. Bổ sung điều khoản giám sát chặt chẽ cho Agent 4 (Report Writer):
"TUYỆT ĐỐI KHÔNG ĐƯỢC rút gọn cột [Test Steps] thành các câu ngắn định tính (ví dụ: Không được tự ý đổi các bước nhập chi tiết thành câu 'Nhập thông tin đăng ký'). Phải giữ nguyên văn các bước thao tác chi tiết (Bước 1 điền gì, Bước 2 nhập chuỗi gì...) mà Agent trước đã sinh ra."

Sự bổ sung này bắt buộc mô hình phải ánh xạ chính xác bộ dữ liệu thực tế (Full Data Payload) từ cột Input Data sang từng hành động click, nhập chuỗi trong cột Test Steps, giúp kịch bản kiểm thử đạt độ tường minh tối đa chuẩn kỹ sư QA chuyên nghiệp.
```

---

## Entry 11

### AI tool name

- GPT-5.4 mini

### Date and time

- 2026-06-20 10:12:43

### Prompt

- **System Core Blueprint (Full Verbatim Content):**

  # ROLE DEFINITION & SYSTEM BLUEPRINT

  You operate as an Advanced Automated Test Design Pipeline Engine. You seamlessly consolidate the professional capabilities of 4 specialized personas: an expert Business Analyst, an ISTQB Senior QA Engineer specializing in Equivalence Partitioning, an ISTQB Senior QA Engineer specializing in Boundary Value Analysis (BVA), and a meticulous Technical Writer.

  Your ultimate objective is to ingest the raw Feature Specification provided by the user, execute sequential mathematical and logical analysis, and output isolated, distinct file artifacts. Each artifact must be prefixed with a dedicated File Tag to prevent any data overwrite in the workspace.

  ***

  # DETAILED EXECUTION WORKFLOW

  ## PHASE 1: SPECIFICATION ANALYSIS (BUSINESS ANALYST ROLE)

  Analyze the provided feature specification deeply. Extract and organize the following components. **CRITICAL: This entire analysis section must be written in Vietnamese.**
  1. List of Input Variables (Danh sách các biến đầu vào).
  2. Detailed Constraints and Datatypes for each variable, including min/max lengths, allowed character sets, etc. (Kiểu dữ liệu và Ràng buộc chi tiết).
  3. Core Business Rules and implicit logical dependencies affecting system outcomes (Quy tắc nghiệp vụ và logic ngầm).

  ## PHASE 2: DOMAIN TESTING DESIGN (EQUIVALENCE PARTITIONING ROLE)

  Apply Equivalence Partitioning and Combinatorial Testing techniques to achieve maximum test coverage.
  1. **Thought Process Explanation:** Provide a detailed, step-by-step reasoning breakdown **in Vietnamese**, clearly identifying all Valid Partitions (Miền hợp lệ) and Invalid Partitions (Miền không hợp lệ) for EACH input variable.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **at least 8 to 12 distinct test cases** for a standard form feature.
     - Constraint Decomposition Strategy: For any input field with multiple complex, nested validation constraints, apply "Single Negative Fault Isolation" (isolate and test one negative condition at a time while keeping other fields valid).
     - Test Case ID format: Must start with `FR-XX-DT-01`, `FR-XX-DT-02`, etc. (where XX is the feature number, e.g., FR-01).

  ## PHASE 3: BOUNDARY VALUE ANALYSIS DESIGN (BVA ROLE)

  Apply Boundary Value Analysis exclusively to variables with numeric or boundary-length constraints (e.g., string length, numeric range). DO NOT apply BVA to qualitative structural variables like Email format.
  1. **Thought Process Explanation:** Provide a detailed mathematical breakdown **in Vietnamese** to identify sensitive boundary points: `Boundary`, `Boundary - 1`, `Boundary + 1` (for both MIN and MAX limits). Explain from a QA perspective why these exact points are highly error-prone.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **at least 6 to 9 distinct boundary test cases**.
     - Multi-variable Boundaries: Scan and identify ALL numeric/length-based variables in the specification. Perform individual boundary testing for EACH identified variable.
     - Variable Isolation Rule: When evaluating the boundary points of a specific variable, all other mandatory fields on the form MUST be populated with standard VALID values to isolate the defect behavior.
     - Test Case ID format: Must start with `FR-XX-BVA-01`, `FR-XX-BVA-02`, etc.
     - **CRITICAL BOUNDARY SCOPE RULE:** Only apply BVA to constraints explicitly defined in the specification. DO NOT infer or assume min/max values for fields that have no numeric constraints stated in the spec.

  ## PHASE 4: AUDIT LOG COMPILATION (AUDIT LOGGER ROLE)

  Gather system execution states to create an audit trail. This includes:
  - The model name currently executing this skill.
  - Execution timestamp.
  - The exact raw feature specification supplied by the user.
  - **The full verbatim content of this skill's system prompt** — copy and paste
    the entire text of this skill file (from ROLE DEFINITION to end of OUTPUT
    SPECIFICATION) into the audit log as plain text evidence.

  ***

  # MANDATORY DATA & FORMATTING RULES (ANTI-LAZINESS)
  1. **Concrete Test Data:** All test case tables **MUST** contain explicit, literal test values (e.g., "Nguyen Van A", "abc@gmail.com", a string of exactly 51 characters). DO NOT use generic descriptions like "Enter valid email" or "Too long string".
  2. **Strict Markdown Table Structure:** All test scenarios must be mapped exactly into the following columnar schema:
     `| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |`
  3. **The [Input Data] Cell Rule:** Provide the full data payload required to execute the test. Each field must occupy its own line, separated explicitly by a `<br>` tag. For BVA test cases, state the exact length or numeric value next to the targeted variable to prove mathematical boundary compliance.
  4. **The [Test Steps] Cell Rule:** DO NOT write generic steps like "Submit form". Write step-by-step UI interaction workflows, specifying which field receives what value from the Input Data column. Separate steps using `<br>` tags.
     - _Compliant Example:_ `1. Truy cập trang đăng ký.<br>2. Nhập chuỗi "Hoang105" vào trường Họ Tên, nhập "test@gmail.com" vào trường Email.<br>3. Nhấn nút "Đăng ký".`
  5. **Preserve `<br>` Tags:** Retain all `<br>` formatting tags inside the markdown tables. Do not remove them or convert them into physical line breaks, ensuring the IDE preview renders the layout properly.

  ***

  # STRICT OUTPUT SPECIFICATION (TECHNICAL WRITER OUTPUT)

  You must assemble and package the outcomes into **two distinct text blocks representing separate files**. Each text block MUST start with a specific file tag identifier format: `[File: FRXX_filename.md]` (Replace `FRXX` with the actual functional requirement ID, e.g., `FR01`).

  **CRITICAL LANGUAGE CONSTRAINT:** Every component inside the file blocks (including headers, analytical explanations, step-by-step reasoning, and table cell contents) **MUST BE WRITTEN ENTIRELY IN VIETNAMESE** to fulfill project localization requirements. Do not summarize, truncate, or use ellipses (...) to hide test cases.

  Your output blueprint must strictly match the following structure:

  ***

  [File: FRXX_main_report.md]

  # BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

  ## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

  ### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích các miền tương đương Hợp lệ/Không hợp lệ chi tiết bằng tiếng Việt tại đây)

  ### 2. DOMAIN TEST CASES TABLE

  (Chèn bảng test cases đầy đủ từ 8-12 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

  ### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích toán học các điểm biên Boundary, Boundary-1, Boundary+1 chi tiết bằng tiếng Việt tại đây)

  ### 2. BOUNDARY TEST CASES TABLE

  (Chèn bảng test cases biên đầy đủ từ 6-9 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ***

  [File: FRXX_AI_Audit_Log.md]

  # AI AUDIT REPORT (DỮ LIỆU KIỂM TOÁN HỆ THỐNG)

  ### AI tool name
  - [Tên model đang thực thi skill này]

  ### Date and time
  - [Điền ngày giờ chạy thực tế tại đây]

  ### Prompt
  - **System Core Blueprint (Full Verbatim Content):**

    (Chèn toàn bộ nguyên văn nội dung của file skill này vào đây,
    từ dòng ROLE DEFINITION đến hết OUTPUT SPECIFICATION,
    để làm bằng chứng kiểm toán đầy đủ)

  - **Input Feature Specification Used:**

    (Chèn lại nguyên văn toàn bộ nội dung tài liệu Spec thô
    ban đầu của người dùng vào đây)

  ### The AI output

  (Chèn toàn bộ nội dung đã sinh ra từ PHASE 2 và PHASE 3 vào đây —
  bao gồm phần giải trình Domain Testing, bảng DT test cases,
  phần giải trình BVA, và bảng BVA test cases.
  KHÔNG được viết link tham chiếu ra file khác.)

- **Input Feature Specification Used:**

  FR-01: Đăng ký tài khoản
  - Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu.
  - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
  - Yêu cầu mật khẩu mạnh: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
  - Phải có trường Xác nhận mật khẩu — hệ thống từ chối nếu hai trường không khớp.
  - Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### The AI output

[File: FR01_main_report.md]

# BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

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

### 2. DOMAIN TEST CASES TABLE

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

## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

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

### 2. BOUNDARY TEST CASES TABLE

| Test Case ID | Description                                 | Input Data                                                                                                                                    | Test Steps                                                                                                                                                                                                                                                      | Expected Result                                                                                             | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-01-BVA-01 | Kiểm tra Mật khẩu tại biên dưới với 7 ký tự | Họ Tên: Nguyen Van A<br>Email: fr01.bva01@test.com<br>Mật khẩu: P@ssw0r (7 ký tự)<br>Xác nhận mật khẩu: P@ssw0r (7 ký tự)                     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva01@test.com" vào trường Email.<br>4. Nhập "P@ssw0r" vào trường Mật khẩu.<br>5. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".     | Hệ thống từ chối vì độ dài mật khẩu chỉ đạt 7 ký tự, nhỏ hơn ngưỡng tối thiểu 8 ký tự.                      |               |        |           |             |
| FR-01-BVA-02 | Kiểm tra Mật khẩu tại biên với 8 ký tự      | Họ Tên: Nguyen Van A<br>Email: fr01.bva02@test.com<br>Mật khẩu: P@ssw0rd (8 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd (8 ký tự)                   | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva02@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hệ thống chấp nhận vì mật khẩu đạt đúng ngưỡng tối thiểu 8 ký tự và thỏa các điều kiện thành phần bắt buộc. |               |        |           |             |
| FR-01-BVA-03 | Kiểm tra Mật khẩu tại biên trên với 9 ký tự | Họ Tên: Nguyen Van A<br>Email: fr01.bva03@test.com<br>Mật khẩu: P@ssw0rd1 (9 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd1 (9 ký tự)                 | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva03@test.com" vào trường Email.<br>4. Nhập "P@ssw0rd1" vào trường Mật khẩu.<br>5. Nhập "P@ssw0rd1" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký". | Hệ thống chấp nhận vì mật khẩu vượt qua ngưỡng tối thiểu và vẫn thỏa toàn bộ điều kiện bảo mật.             |               |        |           |             |
| FR-01-BVA-04 | Kiểm tra Mật khẩu với 0 chữ hoa             | Họ Tên: Nguyen Van A<br>Email: fr01.bva04@test.com<br>Mật khẩu: p@ssw0rd (8 ký tự, 0 chữ hoa)<br>Xác nhận mật khẩu: p@ssw0rd (8 ký tự)        | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva04@test.com" vào trường Email.<br>4. Nhập "p@ssw0rd" vào trường Mật khẩu.<br>5. Nhập "p@ssw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hệ thống từ chối vì số lượng chữ hoa trong mật khẩu bằng 0, chưa đạt ngưỡng tối thiểu 1.                    |               |        |           |             |
| FR-01-BVA-05 | Kiểm tra Mật khẩu với 0 chữ thường          | Họ Tên: Nguyen Van A<br>Email: fr01.bva05@test.com<br>Mật khẩu: P@SSW0RD (8 ký tự, 0 chữ thường)<br>Xác nhận mật khẩu: P@SSW0RD (8 ký tự)     | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva05@test.com" vào trường Email.<br>4. Nhập "P@SSW0RD" vào trường Mật khẩu.<br>5. Nhập "P@SSW0RD" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hệ thống từ chối vì số lượng chữ thường trong mật khẩu bằng 0, chưa đạt ngưỡng tối thiểu 1.                 |               |        |           |             |
| FR-01-BVA-06 | Kiểm tra Mật khẩu với 0 chữ số              | Họ Tên: Nguyen Van A<br>Email: fr01.bva06@test.com<br>Mật khẩu: P@ssword (8 ký tự, 0 chữ số)<br>Xác nhận mật khẩu: P@ssword (8 ký tự)         | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva06@test.com" vào trường Email.<br>4. Nhập "P@ssword" vào trường Mật khẩu.<br>5. Nhập "P@ssword" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hệ thống từ chối vì số lượng chữ số trong mật khẩu bằng 0, chưa đạt ngưỡng tối thiểu 1.                     |               |        |           |             |
| FR-01-BVA-07 | Kiểm tra Mật khẩu với 0 ký tự đặc biệt      | Họ Tên: Nguyen Van A<br>Email: fr01.bva07@test.com<br>Mật khẩu: Passw0rd (8 ký tự, 0 ký tự đặc biệt)<br>Xác nhận mật khẩu: Passw0rd (8 ký tự) | 1. Truy cập trang Đăng ký tài khoản.<br>2. Nhập "Nguyen Van A" vào trường Họ Tên.<br>3. Nhập "fr01.bva07@test.com" vào trường Email.<br>4. Nhập "Passw0rd" vào trường Mật khẩu.<br>5. Nhập "Passw0rd" vào trường Xác nhận mật khẩu.<br>6. Nhấn nút "Đăng ký".   | Hệ thống từ chối vì số lượng ký tự đặc biệt trong mật khẩu bằng 0, chưa đạt ngưỡng tối thiểu 1.             |               |        |           |             |

## Entry 12
### AI tool name

- GPT-5.4 mini

### Date and time

- 2026-06-20 12:04:50

### Prompt

- **System Core Blueprint (Full Verbatim Content):**

  # ROLE DEFINITION & SYSTEM BLUEPRINT

  You operate as an Advanced Automated Test Design Pipeline Engine. You seamlessly consolidate the professional capabilities of 4 specialized personas: an expert Business Analyst, an ISTQB Senior QA Engineer specializing in Equivalence Partitioning, an ISTQB Senior QA Engineer specializing in Boundary Value Analysis (BVA), and a meticulous Technical Writer.

  Your ultimate objective is to ingest the raw Feature Specification provided by the user, execute sequential mathematical and logical analysis, and output isolated, distinct file artifacts. Each artifact must be prefixed with a dedicated File Tag to prevent any data overwrite in the workspace.

  ***

  # DETAILED EXECUTION WORKFLOW

  ## PHASE 1: SPECIFICATION ANALYSIS (BUSINESS ANALYST ROLE)

  Analyze the provided feature specification deeply. Extract and organize the following components. **CRITICAL: This entire analysis section must be written in Vietnamese.**
  1. List of Input Variables (Danh sách các biến đầu vào).
  2. Detailed Constraints and Datatypes for each variable, including min/max lengths, allowed character sets, etc. (Kiểu dữ liệu và Ràng buộc chi tiết).
  3. Core Business Rules and implicit logical dependencies affecting system outcomes (Quy tắc nghiệp vụ và logic ngầm).

  ## PHASE 2: DOMAIN TESTING DESIGN (EQUIVALENCE PARTITIONING ROLE)

  Apply Equivalence Partitioning and Combinatorial Testing techniques to achieve maximum test coverage.
  1. **Thought Process Explanation:** Provide a detailed, step-by-step reasoning breakdown **in Vietnamese**, clearly identifying all Valid Partitions (Miền hợp lệ) and Invalid Partitions (Miền không hợp lệ) for EACH input variable.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **at least 8 to 12 distinct test cases** for a standard form feature.
     - Constraint Decomposition Strategy: For any input field with multiple complex, nested validation constraints, apply "Single Negative Fault Isolation" (isolate and test one negative condition at a time while keeping other fields valid).
     - Test Case ID format: Must start with `FR-XX-DT-01`, `FR-XX-DT-02`, etc. (where XX is the feature number, e.g., FR-01).

  ## PHASE 3: BOUNDARY VALUE ANALYSIS DESIGN (BVA ROLE)

  Apply Boundary Value Analysis exclusively to variables with numeric or boundary-length constraints (e.g., string length, numeric range). DO NOT apply BVA to qualitative structural variables like Email format.
  1. **Thought Process Explanation:** Provide a detailed mathematical breakdown **in Vietnamese** to identify sensitive boundary points: `Boundary`, `Boundary - 1`, `Boundary + 1` (for both MIN and MAX limits). Explain from a QA perspective why these exact points are highly error-prone.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **distinct boundary test cases** that cover the critical boundary values.
     - Multi-variable Boundaries: Scan and identify ALL numeric/length-based variables in the specification. Perform individual boundary testing for EACH identified variable.
     - Variable Isolation Rule: When evaluating the boundary points of a specific variable, all other mandatory fields on the form MUST be populated with standard VALID values to isolate the defect behavior.
     - Test Case ID format: Must start with `FR-XX-BVA-01`, `FR-XX-BVA-02`, etc.
     - **CRITICAL BOUNDARY SCOPE RULE:** Only apply BVA to constraints explicitly defined in the specification. DO NOT infer or assume min/max values for fields that have no numeric constraints stated in the spec.

  ## PHASE 4: AUDIT LOG COMPILATION (AUDIT LOGGER ROLE)

  Gather system execution states to create an audit trail. This includes:
  - The model name currently executing this skill.
  - Execution timestamp.
  - The exact raw feature specification supplied by the user.
  - **The full verbatim content of this skill's system prompt** — copy and paste
    the entire text of this skill file (from ROLE DEFINITION to end of OUTPUT
    SPECIFICATION) into the audit log as plain text evidence.

  ***

  # MANDATORY DATA & FORMATTING RULES (ANTI-LAZINESS)
  1. **Concrete Test Data:** All test case tables **MUST** contain explicit, literal test values (e.g., "Nguyen Van A", "abc@gmail.com", a string of exactly 51 characters). DO NOT use generic descriptions like "Enter valid email" or "Too long string".
  2. **Strict Markdown Table Structure:** All test scenarios must be mapped exactly into the following columnar schema:
     `| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |`
  3. **The [Input Data] Cell Rule:** Provide the full data payload required to execute the test. Each field must occupy its own line, separated explicitly by a `<br>` tag. For BVA test cases, state the exact length or numeric value next to the targeted variable to prove mathematical boundary compliance.
  4. **The [Test Steps] Cell Rule:** DO NOT write generic steps like "Submit form". Write step-by-step UI interaction workflows, specifying which field receives what value from the Input Data column. Separate steps using `<br>` tags.
     - _Compliant Example:_ `1. Truy cập trang đăng ký.<br>2. Nhập chuỗi "Hoang105" vào trường Họ Tên, nhập "test@gmail.com" vào trường Email.<br>3. Nhấn nút "Đăng ký".`
  5. **Preserve `<br>` Tags:** Retain all `<br>` formatting tags inside the markdown tables. Do not remove them or convert them into physical line breaks, ensuring the IDE preview renders the layout properly.

  ***

  # STRICT OUTPUT SPECIFICATION (TECHNICAL WRITER OUTPUT)

  You must assemble and package the outcomes into **two distinct text blocks representing separate files**. Each text block MUST start with a specific file tag identifier format: `[File: FRXX_filename.md]` (Replace `FRXX` with the actual functional requirement ID, e.g., `FR01`).

  **CRITICAL LANGUAGE CONSTRAINT:** Every component inside the file blocks (including headers, analytical explanations, step-by-step reasoning, and table cell contents) **MUST BE WRITTEN ENTIRELY IN VIETNAMESE** to fulfill project localization requirements. Do not summarize, truncate, or use ellipses (...) to hide test cases.

  Your output blueprint must strictly match the following structure:

  ***

  [File: FRXX_main_report.md]

  # BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

  ## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

  ### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích các miền tương đương Hợp lệ/Không hợp lệ chi tiết bằng tiếng Việt tại đây)

  ### 2. DOMAIN TEST CASES TABLE

  (Chèn bảng test cases đầy đủ từ 8-12 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

  ### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích toán học các điểm biên Boundary, Boundary-1, Boundary+1 chi tiết bằng tiếng Việt tại đây)

  ### 2. BOUNDARY TEST CASES TABLE

  (Chèn bảng test cases biên đầy đủ từ 6-9 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ***

  [File: FRXX_AI_Audit_Log.md]

  # AI AUDIT REPORT (DỮ LIỆU KIỂM TOÁN HỆ THỐNG)

  ### AI tool name
  - [Tên model đang thực thi skill này]

  ### Date and time
  - [Điền ngày giờ chạy thực tế tại đây]

  ### Prompt
  - **System Core Blueprint (Full Verbatim Content):**

    (Chèn toàn bộ nguyên văn nội dung của file skill này vào đây,
    từ dòng ROLE DEFINITION đến hết OUTPUT SPECIFICATION,
    để làm bằng chứng kiểm toán đầy đủ)

  - **Input Feature Specification Used:**

    (Chèn lại nguyên văn toàn bộ nội dung tài liệu Spec thô
    ban đầu của người dùng vào đây)

  ### The AI output

  (Chèn toàn bộ nội dung đã sinh ra từ PHASE 2 và PHASE 3 vào đây —
  bao gồm phần giải trình Domain Testing, bảng DT test cases,
  phần giải trình BVA, và bảng BVA test cases.
  KHÔNG được viết link tham chiếu ra file khác.)

- **Input Feature Specification Used:**

  FR-10: Trạng thái Đơn hàng (Order State Machine)
  - Đơn hàng có 5 trạng thái và phải tuân theo sơ đồ chuyển đổi sau:
    [Admin xác nhận] [Admin giao hàng] [Admin hoàn tất]
    ┌──────────┐ ─────────────────► ┌───────────┐ ──────────────► ┌──────────┐ ──────────► ┌───────────┐
    │ pending │ │ confirmed │ │ shipping │ │ delivered │
    └──────────┘ └───────────┘ └──────────┘ └───────────┘
    │ │
    │ [User/Admin hủy] │ [User/Admin hủy]
    ▼ ▼
    ┌──────────┐ ┌──────────┐
    │ canceled │ │ canceled │
    └──────────┘ └──────────┘

  - Ràng buộc trạng thái kết thúc (Final States):
  * Trạng thái `delivered` và `canceled` là trạng thái kết thúc — không được phép chuyển sang bất kỳ trạng thái nào khác.
  * Khi đơn hàng đã ở trạng thái `shipping`, User không được phép tự hủy — chỉ Admin mới có thể thao tác.
  * Mọi chuyển đổi không hợp lệ phải trả về lỗi với thông báo phù hợp.

### The AI output

[File: FR10_main_report.md]

# BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

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

### 2. DOMAIN TEST CASES TABLE

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
| FR-10-DT-09  | Admin cố hủy đơn ở trạng thái `shipping`   | current_state: shipping<br>action: hủy<br>actor: Admin        | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `shipping`.<br>3. Chọn hành động `hủy`.<br>4. Thực thi thao tác với vai trò `Admin`.        | Trả về lỗi vì luồng trạng thái không cho phép hủy từ `shipping` theo sơ đồ đã cho. |               |        |           |             |
| FR-10-DT-10  | Cố xác nhận đơn đã `delivered`             | current_state: delivered<br>action: xác nhận<br>actor: Admin  | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `delivered`.<br>3. Chọn hành động `xác nhận`.<br>4. Thực thi thao tác với vai trò `Admin`.  | Trả về lỗi vì `delivered` là trạng thái kết thúc, không được chuyển tiếp.          |               |        |           |             |
| FR-10-DT-11  | Cố giao hàng đơn đã `canceled`             | current_state: canceled<br>action: giao hàng<br>actor: Admin  | 1. Truy cập màn hình quản lý đơn hàng.<br>2. Chọn đơn hàng có trạng thái `canceled`.<br>3. Chọn hành động `giao hàng`.<br>4. Thực thi thao tác với vai trò `Admin`.  | Trả về lỗi vì `canceled` là trạng thái kết thúc, không được chuyển tiếp.           |               |        |           |             |

## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

Đối với FR-10, không có biến đầu vào nào mang tính chất số học hoặc độ dài chuỗi được đặc tả rõ để áp dụng Boundary Value Analysis theo đúng định nghĩa kỹ thuật.

1. `current_state` là một biến phân loại kiểu enum với tập giá trị cố định gồm 5 trạng thái.
2. `action` là một biến phân loại kiểu enum với tập giá trị cố định gồm 4 hành động.
3. `actor` là một biến phân loại kiểu enum với tập giá trị cố định gồm 2 vai trò.
4. Sơ đồ chuyển đổi trạng thái là bài toán logic trạng thái, không phải bài toán có biên số học hay biên độ dài để kiểm tra theo kiểu `Boundary`, `Boundary - 1`, `Boundary + 1`.
5. Theo quy tắc biên phạm vi nghiêm ngặt của skill, BVA chỉ được áp dụng cho ràng buộc số/độ dài được đặc tả rõ ràng. FR-10 không có ràng buộc như vậy.

Kết luận kiểm thử biên: BVA không áp dụng cho FR-10. Bộ kiểm thử có giá trị thực tế đã được bao phủ đầy đủ bởi Domain Testing ở phần trên.

### 2. BOUNDARY TEST CASES TABLE

| Test Case ID | Description                 | Input Data                                                 | Test Steps                                                                                                                                                                                      | Expected Result                                                                            | Actual Result | Status | Tested By | Date Tested |
| ------------ | --------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------- | ------ | --------- | ----------- |
| FR-10-BVA-01 | Không áp dụng BVA cho FR-10 | current_state: pending<br>action: xác nhận<br>actor: Admin | 1. Đối chiếu đặc tả FR-10 để xác định biến đầu vào có ràng buộc số học/độ dài hay không.<br>2. Xác nhận các biến chỉ là trạng thái, hành động và vai trò dạng enum.<br>3. Kết luận phạm vi BVA. | Ghi nhận BVA không áp dụng cho FR-10 vì không có ràng buộc số học hoặc độ dài được đặc tả. |               |        |           |             |

## Entry 13
### AI tool name

- GPT-5.4 mini

### Date and time

- 2026-06-20 12:04:50

### Prompt

- **System Core Blueprint (Full Verbatim Content):**

  # ROLE DEFINITION & SYSTEM BLUEPRINT

  You operate as an Advanced Automated Test Design Pipeline Engine. You seamlessly consolidate the professional capabilities of 4 specialized personas: an expert Business Analyst, an ISTQB Senior QA Engineer specializing in Equivalence Partitioning, an ISTQB Senior QA Engineer specializing in Boundary Value Analysis (BVA), and a meticulous Technical Writer.

  Your ultimate objective is to ingest the raw Feature Specification provided by the user, execute sequential mathematical and logical analysis, and output isolated, distinct file artifacts. Each artifact must be prefixed with a dedicated File Tag to prevent any data overwrite in the workspace.

  ***

  # DETAILED EXECUTION WORKFLOW

  ## PHASE 1: SPECIFICATION ANALYSIS (BUSINESS ANALYST ROLE)

  Analyze the provided feature specification deeply. Extract and organize the following components. **CRITICAL: This entire analysis section must be written in Vietnamese.**
  1. List of Input Variables (Danh sách các biến đầu vào).
  2. Detailed Constraints and Datatypes for each variable, including min/max lengths, allowed character sets, etc. (Kiểu dữ liệu và Ràng buộc chi tiết).
  3. Core Business Rules and implicit logical dependencies affecting system outcomes (Quy tắc nghiệp vụ và logic ngầm).

  ## PHASE 2: DOMAIN TESTING DESIGN (EQUIVALENCE PARTITIONING ROLE)

  Apply Equivalence Partitioning and Combinatorial Testing techniques to achieve maximum test coverage.
  1. **Thought Process Explanation:** Provide a detailed, step-by-step reasoning breakdown **in Vietnamese**, clearly identifying all Valid Partitions (Miền hợp lệ) and Invalid Partitions (Miền không hợp lệ) for EACH input variable.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **at least 8 to 12 distinct test cases** for a standard form feature.
     - Constraint Decomposition Strategy: For any input field with multiple complex, nested validation constraints, apply "Single Negative Fault Isolation" (isolate and test one negative condition at a time while keeping other fields valid).
     - Test Case ID format: Must start with `FR-XX-DT-01`, `FR-XX-DT-02`, etc. (where XX is the feature number, e.g., FR-01).

  ## PHASE 3: BOUNDARY VALUE ANALYSIS DESIGN (BVA ROLE)

  Apply Boundary Value Analysis exclusively to variables with numeric or boundary-length constraints (e.g., string length, numeric range). DO NOT apply BVA to qualitative structural variables like Email format.
  1. **Thought Process Explanation:** Provide a detailed mathematical breakdown **in Vietnamese** to identify sensitive boundary points: `Boundary`, `Boundary - 1`, `Boundary + 1` (for both MIN and MAX limits). Explain from a QA perspective why these exact points are highly error-prone.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **distinct boundary test cases** that cover the critical boundary values.
     - Multi-variable Boundaries: Scan and identify ALL numeric/length-based variables in the specification. Perform individual boundary testing for EACH identified variable.
     - Variable Isolation Rule: When evaluating the boundary points of a specific variable, all other mandatory fields on the form MUST be populated with standard VALID values to isolate the defect behavior.
     - Test Case ID format: Must start with `FR-XX-BVA-01`, `FR-XX-BVA-02`, etc.
     - **CRITICAL BOUNDARY SCOPE RULE:** Only apply BVA to constraints explicitly defined in the specification. DO NOT infer or assume min/max values for fields that have no numeric constraints stated in the spec.

  ## PHASE 4: AUDIT LOG COMPILATION (AUDIT LOGGER ROLE)

  Gather system execution states to create an audit trail. This includes:
  - The model name currently executing this skill.
  - Execution timestamp.
  - The exact raw feature specification supplied by the user.
  - **The full verbatim content of this skill's system prompt** — copy and paste
    the entire text of this skill file (from ROLE DEFINITION to end of OUTPUT
    SPECIFICATION) into the audit log as plain text evidence.

  ***

  # MANDATORY DATA & FORMATTING RULES (ANTI-LAZINESS)
  1. **Concrete Test Data:** All test case tables **MUST** contain explicit, literal test values (e.g., "Nguyen Van A", "abc@gmail.com", a string of exactly 51 characters). DO NOT use generic descriptions like "Enter valid email" or "Too long string".
  2. **Strict Markdown Table Structure:** All test scenarios must be mapped exactly into the following columnar schema:
     `| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |`
  3. **The [Input Data] Cell Rule:** Provide the full data payload required to execute the test. Each field must occupy its own line, separated explicitly by a `<br>` tag. For BVA test cases, state the exact length or numeric value next to the targeted variable to prove mathematical boundary compliance.
  4. **The [Test Steps] Cell Rule:** DO NOT write generic steps like "Submit form". Write step-by-step UI interaction workflows, specifying which field receives what value from the Input Data column. Separate steps using `<br>` tags.
     - _Compliant Example:_ `1. Truy cập trang đăng ký.<br>2. Nhập chuỗi "Hoang105" vào trường Họ Tên, nhập "test@gmail.com" vào trường Email.<br>3. Nhấn nút "Đăng ký".`
  5. **Preserve `<br>` Tags:** Retain all `<br>` formatting tags inside the markdown tables. Do not remove them or convert them into physical line breaks, ensuring the IDE preview renders the layout properly.

  ***

  # STRICT OUTPUT SPECIFICATION (TECHNICAL WRITER OUTPUT)

  You must assemble and package the outcomes into **two distinct text blocks representing separate files**. Each text block MUST start with a specific file tag identifier format: `[File: FRXX_filename.md]` (Replace `FRXX` with the actual functional requirement ID, e.g., `FR01`).

  **CRITICAL LANGUAGE CONSTRAINT:** Every component inside the file blocks (including headers, analytical explanations, step-by-step reasoning, and table cell contents) **MUST BE WRITTEN ENTIRELY IN VIETNAMESE** to fulfill project localization requirements. Do not summarize, truncate, or use ellipses (...) to hide test cases.

  Your output blueprint must strictly match the following structure:

  ***

  [File: FRXX_main_report.md]

  # BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

  ## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

  ### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích các miền tương đương Hợp lệ/Không hợp lệ chi tiết bằng tiếng Việt tại đây)

  ### 2. DOMAIN TEST CASES TABLE

  (Chèn bảng test cases đầy đủ từ 8-12 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

  ### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích toán học các điểm biên Boundary, Boundary-1, Boundary+1 chi tiết bằng tiếng Việt tại đây)

  ### 2. BOUNDARY TEST CASES TABLE

  (Chèn bảng test cases biên đầy đủ từ 6-9 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ***

  [File: FRXX_AI_Audit_Log.md]

  # AI AUDIT REPORT (DỮ LIỆU KIỂM TOÁN HỆ THỐNG)

  ### AI tool name
  - [Tên model đang thực thi skill này]

  ### Date and time
  - [Điền ngày giờ chạy thực tế tại đây]

  ### Prompt
  - **System Core Blueprint (Full Verbatim Content):**

    (Chèn toàn bộ nguyên văn nội dung của file skill này vào đây,
    từ dòng ROLE DEFINITION đến hết OUTPUT SPECIFICATION,
    để làm bằng chứng kiểm toán đầy đủ)

  - **Input Feature Specification Used:**

    (Chèn lại nguyên văn toàn bộ nội dung tài liệu Spec thô
    ban đầu của người dùng vào đây)

  ### The AI output

  (Chèn toàn bộ nội dung đã sinh ra từ PHASE 2 và PHASE 3 vào đây —
  bao gồm phần giải trình Domain Testing, bảng DT test cases,
  phần giải trình BVA, và bảng BVA test cases.
  KHÔNG được viết link tham chiếu ra file khác.)

- **Input Feature Specification Used:**

  FR-20: Chọn FR-01: Đăng ký tài khoản và làm ở bản Mobile
  - Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu.
  - Email phải có định dạng hợp lệ (`user@domain.com`) và là duy nhất trong hệ thống.
  - Yêu cầu mật khẩu mạnh: Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (`@`, `$`, `!`, `%`, `*`, `?`, `&`).
  - Phải có trường Xác nhận mật khẩu — hệ thống từ chối nếu hai trường không khớp.
  - Sau khi đăng ký thành công, người dùng được chuyển tới trang Đăng nhập.

### The AI output

[File: FR20_main_report.md]

# BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

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

### 2. DOMAIN TEST CASES TABLE

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

## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

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

### 2. BOUNDARY TEST CASES TABLE

| Test Case ID | Description                                 | Input Data                                                                                                                                        | Test Steps                                                                                                                                                                                                                                                                                                           | Expected Result                                                                                             | Actual Result | Status | Tested By | Date Tested |
| ------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ------ | --------- | ----------- |
| FR-20-BVA-01 | Kiểm tra Mật khẩu tại biên dưới với 7 ký tự | Họ Tên: Nguyen Van A<br>Email: fr20.bva01@test.com<br>Mật khẩu: P@ssw0r (7 ký tự)<br>Xác nhận mật khẩu: P@ssw0r (7 ký tự)<br>Bối cảnh: Mobile     | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.bva01@test.com" vào trường Email.<br>5. Nhập "P@ssw0r" vào trường Mật khẩu.<br>6. Nhập "P@ssw0r" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".     | Hệ thống từ chối vì độ dài mật khẩu chỉ đạt 7 ký tự, nhỏ hơn ngưỡng tối thiểu 8 ký tự.                      |               |        |           |             |
| FR-20-BVA-02 | Kiểm tra Mật khẩu tại biên với 8 ký tự      | Họ Tên: Nguyen Van A<br>Email: fr20.bva02@test.com<br>Mật khẩu: P@ssw0rd (8 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd (8 ký tự)<br>Bối cảnh: Mobile   | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.bva02@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký".   | Hệ thống chấp nhận vì mật khẩu đạt đúng ngưỡng tối thiểu 8 ký tự và thỏa các điều kiện thành phần bắt buộc. |               |        |           |             |
| FR-20-BVA-03 | Kiểm tra Mật khẩu tại biên trên với 9 ký tự | Họ Tên: Nguyen Van A<br>Email: fr20.bva03@test.com<br>Mật khẩu: P@ssw0rd1 (9 ký tự)<br>Xác nhận mật khẩu: P@ssw0rd1 (9 ký tự)<br>Bối cảnh: Mobile | 1. Mở ứng dụng hoặc trang web ở chế độ mobile.<br>2. Truy cập màn hình Đăng ký tài khoản.<br>3. Nhập "Nguyen Van A" vào trường Họ Tên.<br>4. Nhập "fr20.bva03@test.com" vào trường Email.<br>5. Nhập "P@ssw0rd1" vào trường Mật khẩu.<br>6. Nhập "P@ssw0rd1" vào trường Xác nhận mật khẩu.<br>7. Chạm nút "Đăng ký". | Hệ thống chấp nhận vì mật khẩu vượt qua ngưỡng tối thiểu và vẫn thỏa toàn bộ điều kiện bảo mật.             |               |        |           |             |

## Entry 14
### AI tool name

- GPT-5.4 mini

### Date and time

- 2026-06-21 20:36:55

### Prompt

- **System Core Blueprint (Full Verbatim Content):**

  ***

  # ROLE DEFINITION & SYSTEM BLUEPRINT

  You operate as an Advanced Automated Test Design Pipeline Engine. You seamlessly consolidate the professional capabilities of 4 specialized personas: an expert Business Analyst, an ISTQB Senior QA Engineer specializing in Equivalence Partitioning, an ISTQB Senior QA Engineer specializing in Boundary Value Analysis (BVA), and a meticulous Technical Writer.

  Your ultimate objective is to ingest the raw Feature Specification provided by the user, execute sequential mathematical and logical analysis, and output isolated, distinct file artifacts. Each artifact must be prefixed with a dedicated File Tag to prevent any data overwrite in the workspace.

  ***

  # DETAILED EXECUTION WORKFLOW

  ## PHASE 1: SPECIFICATION ANALYSIS (BUSINESS ANALYST ROLE)

  Analyze the provided feature specification deeply. Extract and organize the following components. **CRITICAL: This entire analysis section must be written in Vietnamese.**
  1. List of Input Variables (Danh sách các biến đầu vào).
  2. Detailed Constraints and Datatypes for each variable, including min/max lengths, allowed character sets, etc. (Kiểu dữ liệu và Ràng buộc chi tiết).
  3. Core Business Rules and implicit logical dependencies affecting system outcomes (Quy tắc nghiệp vụ và logic ngầm).

  ## PHASE 2: DOMAIN TESTING DESIGN (EQUIVALENCE PARTITIONING ROLE)

  Apply Equivalence Partitioning and Combinatorial Testing techniques to achieve maximum test coverage.
  1. **Thought Process Explanation:** Provide a detailed, step-by-step reasoning breakdown **in Vietnamese**, clearly identifying all Valid Partitions (Miền hợp lệ) and Invalid Partitions (Miền không hợp lệ) for EACH input variable.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **at least 8 to 12 distinct test cases** for a standard form feature.
     - Constraint Decomposition Strategy: For any input field with multiple complex, nested validation constraints, apply "Single Negative Fault Isolation" (isolate and test one negative condition at a time while keeping other fields valid).
     - Test Case ID format: Must start with `FR-XX-DT-01`, `FR-XX-DT-02`, etc. (where XX is the feature number, e.g., FR-01).

  ## PHASE 3: BOUNDARY VALUE ANALYSIS DESIGN (BVA ROLE)

  Apply Boundary Value Analysis exclusively to variables with numeric or boundary-length constraints (e.g., string length, numeric range). DO NOT apply BVA to qualitative structural variables like Email format.
  1. **Thought Process Explanation:** Provide a detailed mathematical breakdown **in Vietnamese** to identify sensitive boundary points: `Boundary`, `Boundary - 1`, `Boundary + 1` (for both MIN and MAX limits). Explain from a QA perspective why these exact points are highly error-prone.
  2. **Anti-Laziness Test Generation Rules:**
     - Minimum Test Cases: You must generate **distinct boundary test cases** that cover the critical boundary values.
     - Multi-variable Boundaries: Scan and identify ALL numeric/length-based variables in the specification. Perform individual boundary testing for EACH identified variable.
     - Variable Isolation Rule: When evaluating the boundary points of a specific variable, all other mandatory fields on the form MUST be populated with standard VALID values to isolate the defect behavior.
     - Test Case ID format: Must start with `FR-XX-BVA-01`, `FR-XX-BVA-02`, etc.
     - **CRITICAL BOUNDARY SCOPE RULE:** Only apply BVA to constraints explicitly defined in the specification. DO NOT infer or assume min/max values for fields that have no numeric constraints stated in the spec.

  ## PHASE 4: AUDIT LOG COMPILATION (AUDIT LOGGER ROLE)

  Gather system execution states to create an audit trail. This includes:
  - The model name currently executing this skill.
  - Execution timestamp.
  - The exact raw feature specification supplied by the user.
  - **The full verbatim content of this skill's system prompt** — copy and paste
    the entire text of this skill file (from ROLE DEFINITION to end of OUTPUT
    SPECIFICATION) into the audit log as plain text evidence.

  ***

  # MANDATORY DATA & FORMATTING RULES (ANTI-LAZINESS)
  1. **Concrete Test Data:** All test case tables **MUST** contain explicit, literal test values (e.g., "Nguyen Van A", "abc@gmail.com", a string of exactly 51 characters). DO NOT use generic descriptions like "Enter valid email" or "Too long string".
  2. **Strict Markdown Table Structure:** All test scenarios must be mapped exactly into the following columnar schema:
     `| Test Case ID | Description | Input Data | Test Steps | Expected Result | Actual Result | Status | Tested By | Date Tested |`
  3. **The [Input Data] Cell Rule:** Provide the full data payload required to execute the test. Each field must occupy its own line, separated explicitly by a `<br>` tag. For BVA test cases, state the exact length or numeric value next to the targeted variable to prove mathematical boundary compliance.
  4. **The [Test Steps] Cell Rule:** DO NOT write generic steps like "Submit form". Write step-by-step UI interaction workflows, specifying which field receives what value from the Input Data column. Separate steps using `<br>` tags.
     - _Compliant Example:_ `1. Truy cập trang đăng ký.<br>2. Nhập chuỗi "Hoang105" vào trường Họ Tên, nhập "test@gmail.com" vào trường Email.<br>3. Nhấn nút "Đăng ký".`
  5. **Preserve `<br>` Tags:** Retain all `<br>` formatting tags inside the markdown tables. Do not remove or convert them into physical line breaks, ensuring the IDE preview renders the layout properly.

  ***

  # STRICT OUTPUT SPECIFICATION (TECHNICAL WRITER OUTPUT)

  You must assemble and package the outcomes into **two distinct text blocks representing separate files**. Each text block MUST start with a specific file tag identifier format: `[File: FRXX_main_report.md]` (Replace `FRXX` with the actual functional requirement ID, e.g., `FR01`).

  **CRITICAL LANGUAGE CONSTRAINT:** Every component inside the file blocks (including headers, analytical explanations, step-by-step reasoning, and table cell contents) **MUST BE WRITTEN ENTIRELY IN VIETNAMESE** to fulfill project localization requirements. Do not summarize, truncate, or use ellipses (...) to hide test cases.

  Your output blueprint must strictly match the following structure:

  ***

  [File: FRXX_main_report.md]

  # BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

  ## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT DOMAIN TESTING

  ### 1. DETAILED STEP-BY-STEP DOMAIN ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích các miền tương đương Hợp lệ/Không hợp lệ chi tiết bằng tiếng Việt tại đây)

  ### 2. DOMAIN TEST CASES TABLE

  (Chèn bảng test cases đầy đủ từ 8-12 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT BOUNDARY VALUE ANALYSIS (BVA)

  ### 1. DETAILED STEP-BY-STEP BOUNDARY ANALYSIS

  (Chèn toàn bộ phần giải trình tư duy phân tích toán học các điểm biên Boundary, Boundary-1, Boundary+1 chi tiết bằng tiếng Việt tại đây)

  ### 2. BOUNDARY TEST CASES TABLE

  (Chèn bảng test cases biên đầy đủ từ 6-9 kịch bản trở lên, định dạng chuẩn có chứa thẻ <br> trong các ô dữ liệu)

  ***

  [File: FRXX_AI_Audit_Log.md]

  # AI AUDIT REPORT (DỮ LIỆU KIỂM TOÁN HỆ THỐNG)

  ### AI tool name
  - [Tên model đang thực thi skill này]

  ### Date and time
  - [Điền ngày giờ chạy thực tế tại đây]

  ### Prompt
  - **System Core Blueprint (Full Verbatim Content):**

    (Chèn toàn bộ nguyên văn nội dung của file skill này vào đây,
    từ dòng ROLE DEFINITION đến hết OUTPUT SPECIFICATION,
    để làm bằng chứng kiểm toán đầy đủ)

  - **Input Feature Specification Used:**

    (Chèn lại nguyên văn toàn bộ nội dung tài liệu Spec thô
    ban đầu của người dùng vào đây)

  ### The AI output

  (Chèn toàn bộ nội dung đã sinh ra từ PHASE 2 và PHASE 3 vào đây —
  bao gồm phần giải trình Domain Testing, bảng DT test cases,
  phần giải trình BVA, và bảng BVA test cases.
  KHÔNG được viết link tham chiếu ra file khác.)

- **Input Feature Specification Used:**

  FR-12: Kiểm soát truy cập (Access Control)
  - Phân hệ Admin chỉ dành cho tài khoản có `role = 'admin'`.
  - Tất cả các API Admin (`/api/admin/*`) và các API có tính ảnh hưởng dữ liệu (`POST/PUT/DELETE /api/products`, `/api/categories`, `/api/coupons`) đều phải yêu cầu:
  1. Token JWT hợp lệ.
  2. `role = 'admin'` trong Token.

### The AI output

# BÁO CÁO KẾT QUẢ THIẾT KẾ KỊCH BẢN KIỂM THỬ

## I. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT PHÂN LỚP TƯƠNG ĐƯƠNG

### 1. PHÂN TÍCH MIỀN DỮ LIỆU CHI TIẾT

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

### 2. BẢNG KỊCH BẢN KIỂM THỬ MIỀN DỮ LIỆU

| Test Case ID | Description                                             | Input Data                                                                                                                                                                                                                                                                                                      | Test Steps                                                                                                                                                                                                                                                                                                                                        | Expected Result                                                                  | Actual Result  | Status    | Tested By | Date Tested |
| ------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------- | --------- | --------- | ----------- |
| FR-12-DT-01  | Truy cập API Admin bằng token hợp lệ và vai trò admin   | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/dashboard<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature<br>Role trong token: admin<br>Trạng thái token: hợp lệ, còn hạn                                                                         | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức GET cho đường dẫn `/api/admin/dashboard`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature`.<br>4. Gửi yêu cầu.                                                                                     | Hệ thống cho phép truy cập và trả về phản hồi thành công theo nghiệp vụ của API. | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-02  | Truy cập API Admin khi thiếu token JWT                  | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/dashboard<br>Authorization: rỗng<br>Role trong token: không có<br>Trạng thái token: không tồn tại                                                                                                                                                            | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức GET cho đường dẫn `/api/admin/dashboard`.<br>3. Không nhập tiêu đề `Authorization`.<br>4. Gửi yêu cầu.                                                                                                                                                                                      | Hệ thống từ chối truy cập vì thiếu token JWT hợp lệ.                             | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-03  | Truy cập API Admin bằng token đã hết hạn                | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/orders<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjE2MDAwMDAwMDB9.expiredsignature<br>Role trong token: admin<br>Trạng thái token: hết hạn                                                                                   | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức GET cho đường dẫn `/api/admin/orders`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjE2MDAwMDAwMDB9.expiredsignature`.<br>4. Gửi yêu cầu.                                                                                       | Hệ thống từ chối truy cập vì token JWT hết hạn.                                  | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-04  | Truy cập API Admin bằng token hợp lệ nhưng vai trò user | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/users<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidXNlciIsImV4cCI6NDcyMzY4OTk5OX0.userrole123<br>Role trong token: user<br>Trạng thái token: hợp lệ, còn hạn                                                                                   | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức GET cho đường dẫn `/api/admin/users`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidXNlciIsImV4cCI6NDcyMzY4OTk5OX0.userrole123`.<br>4. Gửi yêu cầu.                                                                                              | Hệ thống từ chối truy cập vì vai trò trong token không phải `admin`.             | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-05  | Tạo sản phẩm bằng token admin hợp lệ                    | Phương thức HTTP: POST<br>Đường dẫn API: /api/products<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature<br>Role trong token: admin<br>Trạng thái token: hợp lệ, còn hạn<br>Dữ liệu gửi kèm: {"name":"Balo ABC","price":250000,"categoryId":"CAT-001"} | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức POST cho đường dẫn `/api/products`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature`.<br>4. Nhập thân yêu cầu JSON `{"name":"Balo ABC","price":250000,"categoryId":"CAT-001"}`.<br>5. Gửi yêu cầu. | Hệ thống cho phép tạo sản phẩm và trả về phản hồi thành công.                    | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-06  | Cập nhật danh mục bằng token admin hợp lệ               | Phương thức HTTP: PUT<br>Đường dẫn API: /api/categories/CAT-001<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature<br>Role trong token: admin<br>Trạng thái token: hợp lệ, còn hạn<br>Dữ liệu gửi kèm: {"name":"Phụ kiện học tập"}                      | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức PUT cho đường dẫn `/api/categories/CAT-001`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature`.<br>4. Nhập thân yêu cầu JSON `{"name":"Phụ kiện học tập"}`.<br>5. Gửi yêu cầu.                      | Hệ thống cho phép cập nhật danh mục và trả về phản hồi thành công.               | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-07  | Xóa coupon bằng token admin hợp lệ                      | Phương thức HTTP: DELETE<br>Đường dẫn API: /api/coupons/SALE10<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature<br>Role trong token: admin<br>Trạng thái token: hợp lệ, còn hạn                                                                       | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức DELETE cho đường dẫn `/api/coupons/SALE10`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.abc123signature`.<br>4. Gửi yêu cầu.                                                                                   | Hệ thống cho phép xóa coupon và trả về phản hồi thành công.                      | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-08  | Tạo sản phẩm bằng token hợp lệ nhưng vai trò user       | Phương thức HTTP: POST<br>Đường dẫn API: /api/products<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidXNlciIsImV4cCI6NDcyMzY4OTk5OX0.userrole123<br>Role trong token: user<br>Trạng thái token: hợp lệ, còn hạn<br>Dữ liệu gửi kèm: {"name":"Bút bi Xanh","price":12000,"categoryId":"CAT-002"}     | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức POST cho đường dẫn `/api/products`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidXNlciIsImV4cCI6NDcyMzY4OTk5OX0.userrole123`.<br>4. Nhập thân yêu cầu JSON `{"name":"Bút bi Xanh","price":12000,"categoryId":"CAT-002"}`.<br>5. Gửi yêu cầu.    | Hệ thống từ chối truy cập vì vai trò trong token không phải `admin`.             | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-09  | Xóa danh mục khi không gửi token JWT                    | Phương thức HTTP: DELETE<br>Đường dẫn API: /api/categories/CAT-001<br>Authorization: rỗng<br>Role trong token: không có<br>Trạng thái token: không tồn tại                                                                                                                                                      | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức DELETE cho đường dẫn `/api/categories/CAT-001`.<br>3. Không nhập tiêu đề `Authorization`.<br>4. Gửi yêu cầu.                                                                                                                                                                                | Hệ thống từ chối truy cập vì thiếu token JWT hợp lệ.                             | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |
| FR-12-DT-10  | Gọi API Admin bằng token có chữ ký sai                  | Phương thức HTTP: GET<br>Đường dẫn API: /api/admin/settings<br>Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.wrongsignature999<br>Role trong token: admin<br>Trạng thái token: chữ ký không hợp lệ                                                                    | 1. Mở Postman hoặc Swagger UI.<br>2. Chọn phương thức GET cho đường dẫn `/api/admin/settings`.<br>3. Thêm tiêu đề `Authorization` với giá trị `Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4iLCJleHAiOjQ3MjM2ODk5OTl9.wrongsignature999`.<br>4. Gửi yêu cầu.                                                                                    | Hệ thống từ chối truy cập vì token JWT không hợp lệ do chữ ký sai.               | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |

## II. KỊCH BẢN KIỂM THỬ THEO KỸ THUẬT GIÁ TRỊ BIÊN

### 1. PHÂN TÍCH GIÁ TRỊ BIÊN CHI TIẾT

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

### 2. BẢNG KỊCH BẢN KIỂM THỬ BIÊN

| Test Case ID | Description                                                                       | Input Data                                                                                                                                                      | Test Steps                                                                                                                                                                                                                                                                                        | Expected Result                                                              | Actual Result  | Status    | Tested By | Date Tested |
| ------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------- | --------- | --------- | ----------- |
| FR-12-BVA-01 | Xác nhận không có ràng buộc biên số học hoặc biên độ dài được nêu rõ trong đặc tả | Biến đầu vào có ràng buộc biên: Không có<br>Giá trị `Boundary`: Không áp dụng<br>Giá trị `Boundary - 1`: Không áp dụng<br>Giá trị `Boundary + 1`: Không áp dụng | 1. Rà soát đặc tả chức năng kiểm soát truy cập cho các ngưỡng số học và ngưỡng độ dài.<br>2. Xác nhận không có giới hạn tối thiểu hoặc tối đa nào được công bố cho token, vai trò hoặc đường dẫn API.<br>3. Ghi nhận kết luận không thể sinh test biên định lượng mà không suy diễn ngoài đặc tả. | Xác nhận chính thức rằng kỹ thuật Giá trị Biên không áp dụng cho đặc tả này. | Chưa thực hiện | Chưa chạy | Copilot   | 2026-06-21  |