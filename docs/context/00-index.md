# 提案コンテキスト・パック（WDP / Vis）

Mục đích: lưu lại toàn bộ context đã thảo luận về 提案 để **tiếp tục làm việc ở máy local**
mà không mất dữ liệu (chat không tự đồng bộ, chỉ file trong repo mới đi theo).

## Cách dùng ở máy local

```bash
git clone https://github.com/bsj-chaumai/WDP.git
cd WDP
git checkout cursor/proposal-context-pack-f1d5
```

Nếu đã clone sẵn:

```bash
git fetch origin
git checkout cursor/proposal-context-pack-f1d5
```

Sau đó mở thư mục repo bằng Cursor ở máy. Khi chat mới, tham chiếu `@docs/context/`
để agent đọc lại toàn bộ bối cảnh.

## Danh sách tài liệu

| File | Nội dung |
|---|---|
| `10-vis-questionnaire-answers.md` | 10 câu hỏi gửi Vis + câu trả lời gốc (JA) + phân tích (VI) |
| `11-meeting-notes.md` | Nội dung 2 đoạn ghi âm họp với Vis (独立アプリ / AIレポート) |
| `20-agreed-direction.md` | Các điểm đã thống nhất nội bộ: 問題・方向性・提案の軸・次のアクション |
| `30-dev-survey-brief.md` | 要点 khảo sát cho dev (有料化 & survey) |
| `40-proposal-framework.md` | Khung 提案: 背景→課題→方針→絞込→提案(松竹梅)→効果 |

## Tài liệu đã có từ trước (không nằm trong pack này)

- `docs/01-phan-tich-muc-tieu-lon.md` … `docs/06-wdp-wd-xd-flow-ja.html`
- Nguồn gốc: 『ヴィスの現状と今後について』(WDP XD事業計画 / 小川 慧 / 2025-12-26)
- Web chính thức: <https://vis-produce.com/service/data-solution/wdp>,
  <https://vis-produce.com/lp/experience-design>

## Nguyên tắc xuyên suốt

1. Trục 提案 lần này = **有料化** + **survey (gắn 有料化)** + **các yêu cầu KH đã nêu**.
2. **AIレポート ngoài scope BS** — Vis tự làm bằng AI nội bộ, chỉ dùng như ví dụ về tốc độ.
3. Luôn phân biệt **提案用（1 lần, 付加価値）** vs **継続用（定点, nguồn 有料）**.
