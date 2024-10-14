# -*- coding: utf-8 -*-
from configExcel import URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
import importlib.util
import time

# Cargar el módulo DataArray dinámicamente
spec = importlib.util.spec_from_file_location("DataArray", "DataArray.py")
data_array = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_array)

# Obtener todas las variables definidas en el módulo DataArray
variables = data_array.variables

# Inicializar el WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Espera implícita de 10 segundos para que los elementos estén disponibles
driver.get(URL)
driver.maximize_window()
# Espera a que la página cargue completamente
time.sleep(10)

# Usar los nombres de campo directamente desde variables
try:
    from configExcel import URL
    
    
    driver.find_element(By.CSS_SELECTOR, '[name="search_query"]').send_keys(variables.get("campo1", ""))
    driver.find_element(By.CSS_SELECTOR, '.ytp-share-panel-include-playlist-checkbox').send_keys(variables.get("campo2", ""))
    driver.find_element(By.CSS_SELECTOR, '#button').click()
    driver.find_element(By.CSS_SELECTOR, '.yt-spec-button-shape-next.yt-spec-button-shape-next--tonal.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--enable-backdrop-filter-experiment').click()
    driver.find_element(By.CSS_SELECTOR, '.yt-spec-button-shape-next.yt-spec-button-shape-next--text.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-only-default.yt-spec-button-shape-next--enable-backdrop-filter-experiment').click()
    driver.find_element(By.CSS_SELECTOR, '#search-icon-legacy').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-playlist-menu-button.ytp-button.ytp-playlist-menu-button-tiny').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-search-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-cards-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-overflow-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-unmute.ytp-popup.ytp-button.ytp-unmute-animated.ytp-unmute-shrink').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-gated-actions-overlay-miniplayer-close-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-suggested-action-badge-dismiss-button-icon.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-featured-product-overflow-icon.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-large-play-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-featured-product-info-icon.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-suggested-action-badge.ytp-suggested-action-badge-with-controls.ytp-suggested-action-badge-expanded').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-suggested-action-badge.ytp-suggested-action-badge-with-controls').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-mdx-privacy-popup-cancel').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-mdx-privacy-popup-confirm').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-playlist-menu-close.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-share-panel-close.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-watch-later-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-share-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-copylink-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-overflow-panel-close.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-play-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-mute-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-live-badge.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-chapter-title.ytp-button.ytp-chapter-container-disabled').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-fullerscreen-edu-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-subtitles-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-button.ytp-settings-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-miniplayer-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-pip-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-size-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-remote-button.ytp-button').click()
    driver.find_element(By.CSS_SELECTOR, '.ytp-fullscreen-button.ytp-button').click()
    
except NoSuchElementException:
    print("Error: No se encontró uno de los campos.")
except ElementNotInteractableException:
    print("Error: El elemento no es interactuable.")
except TimeoutException:

                print("Error: Tiempo de espera excedido para encontrar el elemento.")

# Finalizar el WebDriver
time.sleep(30)
driver.quit()
