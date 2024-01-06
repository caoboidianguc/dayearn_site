disable certain time
khi khach đặt hẹn trùng hoặc trong khoảng thời gian đang phục vụ, tạo gợi ý cho khách lấy giờ tiêps theo trong ngày hoặc ngày khác


from datetime import datetime, timedelta
 
now_plus_10 = datetime.now() + timedelta(minutes = 10)