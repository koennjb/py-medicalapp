GET_PATIENT_NOTES = ''' SELECT N.content AS Content, N.date AS Date, P.purpose AS Purpose, M.LastName AS Author
        FROM Note N
            JOIN MedicalStaff M ON(M.ID = N.AuthorID)
            JOIN Appointment A ON(A.ID = N.AppointmentId)
            JOIN Purpose P ON(P.Id = A.purposeId)
            JOIN Patient PA ON(PA.id = A.patientId)
        WHERE PA.FirstName LIKE %s AND PA.LastName LIKE %s
    '''
GET_EMPLOYEES = '''SELECT * FROM Employees'''
GET_PATIENT_CONTACTINFO = '''   SELECT FirstName, LastName, Number as PhoneNumber,
                                    Name as PhoneType, StreetAddress, AppNumber, City, State, ZipCode
                                FROM Patient p
                                    JOIN PhoneInfo pi ON (p.ID = pi.personid)
                                    JOIN PhoneType pt ON (pi.typeid= pt.id)
                                    JOIN Address a ON (p.id=a.personid)
                                WHERE p.id = %s
                            '''
