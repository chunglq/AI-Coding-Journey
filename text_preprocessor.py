import re

def load_and_preprocess_text(file_path):
    """
    Load text from file and preprocess it by:
    - Converting to lowercase
    - Removing punctuation and special characters
    - Removing extra whitespace
    - Removing numbers
    """
    # Load text
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Preprocess
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation and numbers
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = text.strip()  # Remove leading/trailing whitespace
    
    return text

# Test the function
if __name__ == "__main__":
    processed_text = load_and_preprocess_text('test.txt')
    print("Original file content:")
    with open('test.txt', 'r') as f:
        print(f.read())
    
    print("\nProcessed text:")
    print(processed_text)