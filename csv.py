import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


# ===== 設定 =====
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")  # 保存ディレクトリ
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})
chrome_options.add_argument("--start-maximized")

# ====== Chromeオプション ======
options = Options()
options.add_argument("--headless")  # ヘッドレスモード（画面非表示）
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    url = "https://www.nasdaq.com/market-activity/stocks/screener"
    driver.get(url)

    time.sleep(5)  # ページ読み込み待ち（JS 完全読み込み）

    # 「Download CSV」ボタンを探してクリック
    # btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Download CSV')]")
    # btn.click()
    btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/article/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/button')  # 要素を取得
    btn.click()  # submitボタンを押す

    print("クリックしました。CSV 保存を待っています…")

    # 適宜待つ（環境による）
    time.sleep(10)

finally:
    driver.quit()

print("完了！保存先:", DOWNLOAD_DIR)