import csv

# Define input CSV file and output PHP file
csv_filename = "colors.csv"
php_filename = "color_classes.php"

# Read class names from the CSV
class_names = []

with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        if len(row) < 2:
            continue  # Skip invalid rows
        
        class_name = row[1]  # Assuming the second column contains the color name
        class_names.append(class_name)

# Generate PHP file content
php_content = "<?php\n\nreturn [\n"
php_content += ",\n".join(f"    '{name}'" for name in class_names)
php_content += "\n];\n"

# Write to PHP file
with open(php_filename, "w", encoding="utf-8") as phpfile:
    phpfile.write(php_content)

print(f"PHP array file '{php_filename}' created successfully!")
