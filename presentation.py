import sys
import re
from application import MarketplaceApp


def split_command_preserve_quotes(command):
    pattern = r"(\"[^\"]*\"|'[^']*'|\S+)"  # 匹配引號包住的內容或獨立單詞
    matches = re.findall(pattern, command)
    return matches


def check_quotes(extracted):
    """
    檢查字串是否在原始輸入中帶有引號。
    """
    return (extracted.startswith("'") and extracted.endswith("'")) or \
           (extracted.startswith('"') and extracted.endswith('"'))


def find_invalid_quotes(original, parsed_args, should_have_quotes=True):
    """
    找出不符合規則的參數：
    - `should_have_quotes=True`：應該要有引號但沒有的參數
    - `should_have_quotes=False`：不該有引號但卻有的參數
    """
    invalid_args = []
    for arg in parsed_args:
        has_quotes = check_quotes(arg)  #檢查有沒有quote
        if should_have_quotes and not has_quotes:
            invalid_args.append(arg)  # 需要引號但沒引號
        if not should_have_quotes and has_quotes:
            invalid_args.append(arg)  # 不該有引號卻有引號
    return invalid_args


def strip_quotes(text):
    """
    去掉字串的引號（如果有的話）。
    """
    if text.startswith(("'", '"')) and text.endswith(("'", '"')):
        return text[1:-1]
    return text


def main():
    app = MarketplaceApp()

    while True:
        command = input("# ").strip()
        if not command:
            continue

        parts = split_command_preserve_quotes(command)  #先保留引號 因為我要檢查使用者是否在該有引號的時候有打
        #這邊會是一個list 然後比如我input是 'Phone model 8' 他的list == ["'Phone model 8'"]

        if len(parts) == 0:
            continue

        action = parts[0]

        if action == "REGISTER":
            if len(parts) != 2:
                print("Error - Invalid command")
                continue

            # 檢查 username **不應該有引號**
            invalid = find_invalid_quotes(command, [parts[1]], should_have_quotes=False)
            if invalid:
                print(f"Error - These parameters should NOT have quotes: {', '.join(invalid)}")
                continue

            print(app.register_user(parts[1]))

        elif action == "CREATE_LISTING":
            if len(parts) != 6:
                print("Error - Invalid command")
                continue

            username, title, description, price, category = parts[1], parts[2], parts[3], parts[4], parts[5]

            invalid_quotes = find_invalid_quotes(command, [title, description, category], should_have_quotes=True)# **檢查 title, description, category 應該要有引號**
            invalid_no_quotes = find_invalid_quotes(command, [username, price], should_have_quotes=False)# **檢查 username, price 不應該有引號**

            if invalid_quotes:
                print(f"Error - These parameters MUST have quotes: {', '.join(invalid_quotes)}") 
            if invalid_no_quotes:
                print(f"Error - These parameters should NOT have quotes: {', '.join(invalid_no_quotes)}")
            if invalid_quotes or invalid_no_quotes:
                continue

            # 移除引號後傳遞到 `application.py`
            print(app.create_listing(username, strip_quotes(title), strip_quotes(description), int(price), strip_quotes(category)))

        elif action == "GET_LISTING":
            if len(parts) != 3:
                print("Error - Invalid command")
                continue

            # **檢查 username 和 listing_id 不應該有引號**
            invalid = find_invalid_quotes(command, [parts[1], parts[2]], should_have_quotes=False)
            if invalid:
                print(f"Error - These parameters should NOT have quotes: {', '.join(invalid)}")
                continue

            print(app.get_listing(parts[1], int(parts[2])))

        elif action == "DELETE_LISTING":
            if len(parts) != 3:
                print("Error - Invalid command")
                continue

            # **檢查 username 和 listing_id 不應該有引號**
            invalid = find_invalid_quotes(command, [parts[1], parts[2]], should_have_quotes=False)
            if invalid:
                print(f"Error - These parameters should NOT have quotes: {', '.join(invalid)}")
                continue

            print(app.delete_listing(parts[1], int(parts[2])))

        elif action == "GET_CATEGORY":
            if len(parts) != 3:
                print("Error - Invalid command")
                continue

            # **檢查 username 不應該有引號，category 應該有引號**
            invalid_no_quotes = find_invalid_quotes(command, [parts[1]], should_have_quotes=False)
            invalid_quotes = find_invalid_quotes(command, [parts[2]], should_have_quotes=True)

            if invalid_no_quotes:
                print(f"Error - These parameters should NOT have quotes: {', '.join(invalid_no_quotes)}")
            if invalid_quotes:
                print(f"Error - These parameters MUST have quotes: {', '.join(invalid_quotes)}")
            if invalid_no_quotes or invalid_quotes:
                continue

            print(app.get_category(parts[1], strip_quotes(parts[2])))

        elif action == "GET_TOP_CATEGORY":
            if len(parts) != 2:
                print("Error - Invalid command")
                continue

            # **檢查 username 不應該有引號**
            invalid = find_invalid_quotes(command, [parts[1]], should_have_quotes=False)
            if invalid:
                print(f"Error - These parameters should NOT have quotes: {', '.join(invalid)}")
                continue

            print(app.get_top_category(parts[1]))

        elif action == "EXIT":
            break

        else:
            print("Error - Invalid command")


if __name__ == "__main__":
    main()