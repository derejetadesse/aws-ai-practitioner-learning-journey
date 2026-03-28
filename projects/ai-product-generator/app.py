def generate_product_description(product_name, features):
    return f"""
Product: {product_name}

Key Features:
{features}

Description:
This high-quality {product_name} is designed to improve daily workflow.
It offers reliability, comfort, and efficiency, making it a great choice for both home and office use.

Bullet Points:
- High quality and durable
- User-friendly design
- Great value for money
"""

if __name__ == "__main__":
    product = input("Enter product name: ")
    features = input("Enter features: ")

    result = generate_product_description(product, features)
    print(result)