document.addEventListener('DOMContentLoaded', () => {
    // Sample data for earnings overview
    document.getElementById('total-earnings').textContent = '1200.50';
    document.getElementById('pending-earnings').textContent = '300.75';
    document.getElementById('completed-sales').textContent = '24';

    // Sample data for earnings breakdown table
    const earningsData = [
        { date: '2024-10-01', orderId: '12345', product: 'Handmade Pottery', amount: '50.00', status: 'Completed' },
        { date: '2024-10-02', orderId: '12346', product: 'Artisan Jewelry', amount: '75.00', status: 'Pending' },
        { date: '2024-10-03', orderId: '12347', product: 'Wooden Crafts', amount: '120.00', status: 'Completed' }
    ];

    const tableBody = document.getElementById('earnings-table-body');
    earningsData.forEach(entry => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${entry.date}</td>
            <td>${entry.orderId}</td>
            <td>${entry.product}</td>
            <td>₹${entry.amount}</td>
            <td>${entry.status}</td>
        `;
        tableBody.appendChild(row);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Sample data for product list
    const productData = [
        { image: '../static/pottery.jpg', name: 'Handmade Pottery', category: 'Pottery', price: '₹45.00', stock: '10' },
        { image: '../static/earring.jpg', name: 'Artisan Jewelry', category: 'Jewelry', price: '₹30.00', stock: '20' },
        { image: '../static/wooden.jpg', name: 'Wooden Crafts', category: 'Woodcraft', price: '₹60.00', stock: '5' }
    ];

    const tableBody = document.getElementById('product-table-body');
    productData.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><img src="${product.image}" alt="${product.name}"></td>
            <td>${product.name}</td>
            <td>${product.category}</td>
            <td>${product.price}</td>
            <td>${product.stock}</td>
            <td>
                <button class="edit-btn"><i class="fas fa-edit"></i></button>
                <button class="delete-btn"><i class="fas fa-trash"></i></button>
            </td>
        `;
        tableBody.appendChild(row);
    });

    const modal = document.getElementById('product-modal');
    const addProductBtn = document.getElementById('add-product-btn');
    const closeBtn = document.getElementsByClassName('close-btn')[0];
    const modalTitle = document.getElementById('modal-title');
    const productForm = document.getElementById('product-form');

    addProductBtn.addEventListener('click', () => {
        modal.style.display = 'block';
        modalTitle.textContent = 'Add New Product';
        productForm.reset();
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });

    productForm.addEventListener('submit', (event) => {
        event.preventDefault();
        // Add logic to handle form submission and updating product list
        modal.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Sample data for orders
    const orderData = [
        { id: 'ORD12345', customerName: 'John Doe', product: 'Handmade Pottery', quantity: 2, totalPrice: '₹90.00', status: 'Shipped' },
        { id: 'ORD12346', customerName: 'Jane Smith', product: 'Artisan Jewelry', quantity: 1, totalPrice: '₹30.00', status: 'Pending' },
        { id: 'ORD12347', customerName: 'Michael Johnson', product: 'Wooden Crafts', quantity: 3, totalPrice: '₹180.00', status: 'Delivered' }
    ];

    const tableBody = document.getElementById('order-table-body');
    orderData.forEach(order => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${order.id}</td>
            <td>${order.customerName}</td>
            <td>${order.product}</td>
            <td>${order.quantity}</td>
            <td>₹${order.totalPrice}</td>
            <td>${order.status}</td>
            <td>
                <button class="view-btn"><i class="fas fa-eye"></i></button>
                <button class="edit-btn"><i class="fas fa-edit"></i></button>
            </td>
        `;
        tableBody.appendChild(row);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const profileForm = document.querySelector('.profile-edit form');
    
    profileForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const formData = new FormData(profileForm);
        const profileData = Object.fromEntries(formData.entries());
        
        // Placeholder for form submission logic
        console.log('Profile Updated:', profileData);
        
        alert('Profile updated successfully!');
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const supportForm = document.getElementById('support-form');
    
    supportForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const formData = new FormData(supportForm);
        const supportData = Object.fromEntries(formData.entries());
        
        // Placeholder for form submission logic
        console.log('Support Request Submitted:', supportData);
        
        alert('Your support request has been submitted!');
    });
});
