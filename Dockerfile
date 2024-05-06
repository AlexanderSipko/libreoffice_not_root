# Используем базовый образ Python 3.10
FROM python:3.10

# Устанавливаем необходимые зависимости
RUN pip install --no-cache-dir fastapi uvicorn

# Устанавливаем unoconv и LibreOffice
RUN apt-get update && apt-get install -y unoconv libreoffice

# Добавляем пользователя appuser, если он еще не существует
RUN if ! id -u appuser > /dev/null 2>&1; then \
        groupadd -r appuser && useradd -r -g appuser appuser; \
    fi

# Копируем код приложения внутрь контейнера
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# # Создаем директории, если они не существуют
# RUN mkdir -p /root/.config && \
RUN mkdir -p /app/output_files && \
    mkdir -p /tmp  && \
    mkdir -p /var && \
    mkdir -p /home/appuser/.config && \
    mkdir -p /home/appuser/.cache/dconf
    # mkdir -p /root/.cache/dconf && \
    
# # Устанавливаем владельца и разрешения для директории приложения
# RUN chown -R appuser:appuser /app

# # Устанавливаем владельца и разрешения для примонтированных томов
# RUN chown -R appuser:appuser /root/.config && \
RUN chown -R appuser:appuser /app/output_files && \
    chown -R appuser:appuser /tmp && \
    chown -R appuser:appuser /var && \
    chown -R appuser:appuser /home/appuser/.config && \
    chown -R appuser:appuser /home/appuser/.cache/dconf
    # chown -R appuser:appuser /root/.cache/dconf && \

# # Устанавливаем пользователя по умолчанию
USER appuser:appuser

# Экспонируем порт, на котором будет работать приложение
EXPOSE 80

# Запускаем сервер с помощью uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]