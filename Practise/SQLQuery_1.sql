-- Create a table called Students
CREATE TABLE Students (
    ID INT IDENTITY(1,1) PRIMARY KEY,   -- Auto-incrementing ID
    Name NVARCHAR(50) NOT NULL,          -- Name column, up to 50 characters
    Age INT NOT NULL,                     -- Age column
    EnrollmentDate DATE DEFAULT GETDATE() -- Optional default value
);
GO
