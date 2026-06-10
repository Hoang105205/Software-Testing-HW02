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


