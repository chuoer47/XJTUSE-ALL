init_comer_record = "INSERT INTO comer_record (requester, responder,start_time) VALUES (?,?, ?)"

update_comer_record = f"UPDATE comer_record SET end_time = ? WHERE requester = ?"

insert_chat_logs = f"INSERT INTO chat_logs (username, message,message_time) VALUES (?, ?,?)"

add_user = f"INSERT INTO users (username, password) VALUES (?, ?)"

find_user = f"SELECT * FROM users WHERE username = ? AND password = ?"