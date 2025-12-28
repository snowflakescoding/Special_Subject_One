// Chờ trang load xong
document.addEventListener('DOMContentLoaded', function() {
    
    // Hiệu ứng xuất hiện lần lượt cho các task (Staggered Animation)
    const tasks = document.querySelectorAll('.task-item');
    tasks.forEach((task, index) => {
        task.style.animationDelay = `${index * 0.1}s`; // Task sau trễ hơn task trước 0.1s
        task.classList.add('fade-in-up');
    });

    // Xác nhận xóa đẹp hơn (Optional)
    const deleteLinks = document.querySelectorAll('.delete-btn');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if(!confirm('Bạn có chắc muốn xóa task này không?')) {
                e.preventDefault();
            }
        });
    });
});