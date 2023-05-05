-- Sellers
INSERT INTO Sellers (SellerID, SellerName, Email, Phone)
VALUES (1, 'Mahmoud', 'mahmoud@gmail.com', '555-1234');

INSERT INTO Sellers (SellerID, SellerName, Email, Phone)
VALUES (2, 'Test_Seller', 'test_seller@test.com', '555-5678');

-- Products
INSERT INTO Products (ProductID, ProductName, Price, Description)
VALUES (1, 'Product A', 10.99, 'A product that make your wife happy');

INSERT INTO Products (ProductID, ProductName, Price, Description)
VALUES (2, 'Product B', 19.99, 'Luxury without the luxury price tag - your wallet will thank you!');

INSERT INTO Products (ProductID, ProductName, Price, Description)
VALUES (3, 'Product C', 5.99, 'The little product with a lot of power!');

INSERT INTO Products (ProductID, ProductName, Price, Description)
VALUES (4, 'Product D', 7.99, 'It can solve almost any problem!');

INSERT INTO Products (ProductID, ProductName, Price, Description)
VALUES (5, 'Product E', 14.99, 'The product that makes you feel like a superhero !');

-- Orders
INSERT INTO Orders (OrderID, OrderDate, SellerID, CustomerName, TotalAmount)
VALUES (1, '2023-04-01', 1, 'Jon', 31.97);

INSERT INTO Orders (OrderID, OrderDate, SellerID, CustomerName, TotalAmount)
VALUES (2, '2023-04-15', 2, 'Lara', 29.98);


-- OrderProducts
INSERT INTO OrderProducts (OrderID, ProductID, Quantity)
VALUES (1, 1, 2);

INSERT INTO OrderProducts (OrderID, ProductID, Quantity)
VALUES (1, 2, 1);

INSERT INTO OrderProducts (OrderID, ProductID, Quantity)
VALUES (2, 3, 3);

INSERT INTO OrderProducts (OrderID, ProductID, Quantity)
VALUES (2, 4, 2);

-- Issues
INSERT INTO Issues (IssueID, IssueDescription, IssueDate, OrderID)
VALUES (1, 'Item was damaged during shipping', '2023-05-01 10:00:00', 1);

INSERT INTO Issues (IssueID, IssueDescription, IssueDate, OrderID)
VALUES (2, 'Wrong item was delivered', '2023-05-03 14:30:00', 2);
