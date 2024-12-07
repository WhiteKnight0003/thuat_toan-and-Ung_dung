def schedule_tasks(n, tasks):
    # Sắp xếp các công việc theo thời điểm kết thúc
    tasks.sort(key=lambda x: x[1])
    
    # Khởi tạo danh sách công việc được chọn
    selected = [tasks[0]]  # Chọn công việc đầu tiên
    last_end = tasks[0][1]  # Thời điểm kết thúc của công việc cuối cùng được chọn
    
    # Duyệt qua các công việc còn lại
    for i in range(1, n):
        start = tasks[i][0]  # Thời điểm bắt đầu của công việc hiện tại
        
        # Nếu thời điểm bắt đầu của công việc hiện tại >= thời điểm kết thúc của công việc cuối
        if start > last_end:
            selected.append(tasks[i])  # Chọn công việc này
            last_end = tasks[i][1]  # Cập nhật thời điểm kết thúc
    
    return len(selected)

# Đọc input
n = int(input())
tasks = []
for _ in range(n):
    start, end = map(int, input().split())
    tasks.append((start, end))

# In kết quả
print(schedule_tasks(n, tasks))