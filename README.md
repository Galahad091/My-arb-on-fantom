# My simple arb bot on Fantom. This also can apply to EVM such as Cronos, Avax, Polygon, etc
Lưu ý: Bot chỉ mang mục đích thử nghiệm và tham khảo
**Các bước chính bot thực hiện bao gồm:**
- Đọc smartcontract và lấy thông tin pools của một số DEXes lớn trên Fantom như Spookyswap, SpiritSwap, trên Cronos có MM Finance, VVS, Crodex
- Lọc ra các pairs tùy theo điều kiện về thanh khoản, token trong pool
- Sử dụng thuật toán DFS, Bellmen Ford để tìm path arbitrage (path từ token A đến token A)
- Sau khi tìm được path, dựa trên reserves để tính xem có cơ hội arbitrage không, chọn ra path có profit lớn nhất
- Tính toán khối lượng swap
- Check lợi nhuận sau khi trừ đi fees
- Nếu lợi nhuận dương, call đến contract để thực hiện swap

**Hạn chế:**
- Bot chỉ check reserves nên không đủ nhanh bằng việc đọc mempool
- Thuật toán tìm path vẫn cần tối ưu thêm
- Contract chưa đủ tối ưu gas
- Chậm :))
