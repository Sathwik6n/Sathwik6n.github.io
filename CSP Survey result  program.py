# Digital Literacy Improvement Program

print("DIGITAL LITERACY MINI PROJECT")
print("-" * 40)

# Data before training
before_upi = 8
before_online = 10
before_email = 12

# Data after training
after_upi = 26
after_online = 34
after_email = 30

# Calculate improvements
upi_improvement = after_upi - before_upi
online_improvement = after_online - before_online
email_improvement = after_email - before_email

# Display results
print("\nSurvey Results")
print("-" * 40)

print("UPI Users")
print("Before Training :", before_upi)
print("After Training  :", after_upi)
print("Improvement     :", upi_improvement)

print("\nOnline Service Users")
print("Before Training :", before_online)
print("After Training  :", after_online)
print("Improvement     :", online_improvement)

print("\nEmail Users")
print("Before Training :", before_email)
print("After Training  :", after_email)
print("Improvement     :", email_improvement)

# Percentage Improvement
upi_percent = (upi_improvement / before_upi) * 100
online_percent = (online_improvement / before_online) * 100
email_percent = (email_improvement / before_email) * 100

print("\nPercentage Improvement")
print("-" * 40)
print("UPI Users            : {:.2f}%".format(upi_percent))
print("Online Service Users : {:.2f}%".format(online_percent))
print("Email Users          : {:.2f}%".format(email_percent))

print("\nConclusion:")
print("Digital literacy training improved the usage of")
print("UPI payments, online services, and email among participants.")
