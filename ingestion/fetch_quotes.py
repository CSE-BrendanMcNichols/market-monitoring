# Load tickers from text file
def load_tickers():
    with open('../tickers.txt', 'r') as file:
        # Read each line, strip whitespace, ignore empty lines
        tickers = [line.strip() for line in file if line.strip()]
    return tickers

# Test it out
if __name__ == "__main__":
    tickers = load_tickers()
    print(f"Found {len(tickers)} tickers:")
    print(tickers[:5])  # Show first 5 tickers