import flet as ft
#%%
def remove_outliers(num_remove, data_original):
    removed_data = []
    data = []
    
    data = data_original.copy()
    for i in range(num_remove*2):
        if i < num_remove:
            max_value = max(data)
            removed_data.append(max_value)
            data.remove(max_value)
        else:
            min_value = min(data)
            removed_data.append(min_value)
            data.remove(min_value)

    return sorted(data), sorted(removed_data)

#%%
def main(page: ft.Page):
    global start_station, end_station

    # GUI的排版
    page.title = "Remove Outliers GUI"
    page.window_width = 700
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    data_original = []

    # 按鈕的function
    def append_click(e):
        number = int(number_textfield.value)#number_textfield.value 取得值
        data_original.append(number)          # data_original.append(number) 將數字一個一個加進去list中
        list_text.value = f'This list is {data_original}'                 # list_text.value 更改顯示的內容
        page.update()
        

    def result_click(e):
        # 可以使用下面寫好的function傳出的變數繼續完成
        data, removed_data = remove_outliers(int(remove_textfield.value), data_original)
        original_data_text.value = f'The original data : {data_original}'            # original_data_text.value 更改顯示的內容
        data_text.value = f'The data with outliers removed : {data}'                    # data_text.value 更改顯示的內容
        removed_data_text.value = f'The outliers : {removed_data}'            # removed_data_text.value 更改顯示的內容
        page.update()                       # page.update() 更新GUI畫面   
        
        
    

    # ------建立物件------
    
    # for number view
    remove_textfield = ft.TextField(label="Number to remove", width=300, text_size=18)
    number_textfield = ft.TextField(label="Input number to list", width=300, text_size=18)

    append_button = ft.ElevatedButton(text=f"Append the number to list", width=300, on_click=append_click)
    list_text = ft.Text("", size=18)
    
    # for result view
    result_button = ft.ElevatedButton(text=f"Run the function", width=300, on_click=result_click)

    original_data_text = ft.Text("", size=18)
    data_text = ft.Text("", size=18)
    removed_data_text = ft.Text("", size=18)

    # ------將物件進行排版------
    page.add(
        remove_textfield,
        number_textfield,
        append_button,
        list_text,
        result_button,
        original_data_text,
        data_text,
        removed_data_text
            )

ft.app(target=main)