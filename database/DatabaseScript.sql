CREATE TABLE Sellers (
    SellerID INT PRIMARY KEY,
    SellerName VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Phone VARCHAR(20)
);

CREATE TABLE Product1 (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    Price FLOAT NOT NULL,
    Description VARCHAR(255)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(50) NOT NULL,
    OrderDate DATETIME NOT NULL,
    TotalAmount FLOAT(10, 2) NOT NULL,
    SellerID INT NOT NULL,
    FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID)
);

CREATE TABLE Issues (
    IssueID INT PRIMARY KEY,
    IssueDescription VARCHAR(255),
    IssueDate DATETIME NOT NULL,
    OrderID INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

CREATE TABLE OrderProducts (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product1(ProductID)
);