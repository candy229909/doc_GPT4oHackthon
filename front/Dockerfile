# 建置階段
FROM node:lts-alpine as build-stage
WORKDIR /app

# 複製 package.json 和 package-lock.json
COPY package*.json ./

# 安裝相依性
RUN npm install

# 複製所有檔案
COPY . .

# 設定環境變數
ARG VUE_APP_BASE_API
ARG VUE_APP_SERVICE_URL
ENV VUE_APP_BASE_API=$VUE_APP_BASE_API
ENV VUE_APP_SERVICE_URL=$VUE_APP_SERVICE_URL

# 建置應用程式
RUN npm run build

# 生產階段
FROM nginx:stable-alpine as production-stage

# 複製建置結果
COPY --from=build-stage /app/dist /usr/share/nginx/html

# 開放端口
EXPOSE 80

# 啟動 Nginx
CMD ["nginx", "-g", "daemon off;"]
