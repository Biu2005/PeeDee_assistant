Giới thiệu

PeeDee Assistant là một trợ lý ảo tiếng Việt, chạy độc lập trên Raspberry Pi, sử dụng AI (Google Gemini API) để trả lời câu hỏi người dùng.

Hỗ trợ giao tiếp bằng giọng nói.

Xử lý đầu vào giọng nói → chuyển thành văn bản → gửi tới API → nhận kết quả → phát lại bằng giọng nói.

Dự án đã được chấp nhận & trình bày tại Hội nghị Khoa học 2024 (VNUHCM-US Conf).

Ứng dụng: trợ lý học tập, hỏi đáp tri thức, hệ thống giao tiếp người – máy (HRI).

Phần cứng sử dụng

Raspberry Pi 3 Model B+

Microphone USB (thu âm giọng nói)

Loa (xuất âm thanh TTS)

Phần mềm & Công nghệ

Ngôn ngữ: Python

API: Google Gemini API (LLM)

Âm thanh:

Speech-to-Text (Google Speech API / Whisper)

Text-to-Speech (gTTS / pyttsx3)

Framework: HTTPS (trao đổi dữ liệu)

Hệ điều hành: Raspberry Pi OS

Tính năng chính

Nhận diện giọng nói tiếng Việt (STT).

Gửi câu hỏi đến Google Gemini API.

Nhận câu trả lời bằng tiếng Việt.

Phát lại phản hồi bằng loa (TTS).

Cách cài đặt

Clone repo

Tải các thư viện yêu cầu

Thêm vào API

Chạy chương 

Cách sử dụng

Nói vào micro → hệ thống ghi âm & nhận diện.

PeeDee gửi câu hỏi lên Gemini API.

Nhận câu trả lời → chuyển thành giọng nói → phát ra loa.

Demo : ở trên phần branch

Hướng phát triển

Tích hợp camera để nhận diện người nói (HRI).

Thêm đa ngôn ngữ (Anh – Việt).

Đưa vào ứng dụng robot giao tiếp.

Tác giả:

Nguyễn Hoàng Minh Quốc

Phạm Mai Diệu Thảo

Phạm Quốc Trung

Phan Nguyễn Thanh Tùng

Lê Bùi Xuân Quang

Nguyễn Trí Thức
