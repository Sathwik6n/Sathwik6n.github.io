# Digital Literacy Assistant App

def show_training_data():
    before_upi = 8
    after_upi = 26

    before_online = 10
    after_online = 34

    before_email = 12
    after_email = 30

    print("\n--- Training Statistics ---")
    print("UPI Users:", before_upi, "->", after_upi)
    print("Online Service Users:", before_online, "->", after_online)
    print("Email Users:", before_email, "->", after_email)

def digital_payment_guide():
    print("\n--- Digital Payment Guide ---")
    print("1. Install a UPI App")
    print("2. Link your bank account")
    print("3. Set UPI PIN")
    print("4. Scan QR Code")
    print("5. Complete Transaction Safely")

def online_services():
    print("\n--- Online Services ---")
    print("1. Aadhaar Services")
    print("2. PAN Services")
    print("3. Scholarship Applications")
    print("4. Government Schemes")

def cyber_security():
    print("\n--- Cyber Security Tips ---")
    print("• Never share OTP")
    print("• Use strong passwords")
    print("• Verify links before clicking")
    print("• Avoid unknown apps")

while True:
    print("\n================================")
    print(" DIGITAL LITERACY ASSISTANT APP ")
    print("================================")
    print("1. View Training Statistics")
    print("2. Digital Payment Guide")
    print("3. Online Services")
    print("4. Cyber Security Tips")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_training_data()
    elif choice == "2":
        digital_payment_guide()
    elif choice == "3":
        online_services()
    elif choice == "4":
        cyber_security()
    elif choice == "5":
        print("Thank you for using Digital Literacy Assistant!")
        break
    else:
        print("Invalid Choice. Try Again.")
