FROM node:latest as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json  ./
COPY package-lock.json ./

RUN npm install react-scripts@3.4.1 -g --silent
COPY ./src ./src
COPY ./public ./public
RUN npm ci --silent

COPY . /app/
RUN npm run build
RUN npm install -g serve
CMD serve -s build -l 3000


# FROM node:latest as build

# WORKDIR /app
# ENV PATH /app/node_modules/.bin:$PATH
# COPY package.json ./
# COPY package-lock.json ./

# RUN npm ci --silent
# RUN npm install react-scripts@3.4.1 -g --silent
# # add app
# COPY . /app/

# # Build production
# RUN npm run build
# RUN npm install -g serve

# ## Start the app on port 3006
# CMD serve -s build -l 3006

