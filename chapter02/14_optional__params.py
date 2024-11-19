def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:
    """
    Returns a string representing a data in the format "dd/mm/yyyy".

    Args:
        day: The day of month. Default value to 1.
        month: The month of the year. Default value to 1.
        year: The year. Default value to 2000.
    
    Returns:
        The formatted date string.
    """
    return f"{day:02d}/{month:02d}/{year:4d}"

def main():
    print(get_formatted_date()) # 01/01/2000
    print(get_formatted_date(10)) # 10/01/2000
    print(get_formatted_date(14, 5)) # 14/05/2000
    print(get_formatted_date(14, 5, 2024)) # 14/05/2024

    print(get_formatted_date(year=2024)) # 01/01/2024
    print(get_formatted_date(year=2024, day=14, month=5)) # 14/05/2024


if __name__ == "__main__":
    main()