class StudentNotFoundException(Exception):
    """Raised when a student is not found in the system."""
    pass

class CourseNotFoundException(Exception):
    """Raised when a course is not found in the system."""
    pass

class TeacherNotFoundException(Exception):
    """Raised when a teacher is not found in the system."""
    pass

class DuplicateEnrollmentException(Exception):
    """Raised when a student is already enrolled in a course."""
    pass

class PaymentValidationException(Exception):
    """Raised when an invalid payment amount is provided."""
    pass

class InvalidStudentDataException(Exception):
    """Raised when student data is invalid or missing."""
    pass

class InvalidCourseDataException(Exception):
    """Raised when course data is invalid or missing."""
    pass

class InvalidEnrollmentDataException(Exception):
    """Raised when enrollment data is invalid."""
    pass

class InvalidTeacherDataException(Exception):
    """Raised when teacher data is invalid."""
    pass

class InsufficientFundsException(Exception):
    """Raised when a student does not have sufficient funds for a payment."""
    pass
