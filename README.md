# BaiCiZhanPrinter

BaiCiZhanPrinter 可以将手机端APP百词斩中的已背单词表导出。

## 特性

- 支持导出为`xlsx`或`html`格式文件，`html`文件可以在浏览器中进一步转换为`pdf`。
- 提供两种导出模板：**默认模板和默写模板**，默写模板支持指定空白列数量。
- 支持两种排序方式：**字母顺序和随机**。

## 安装依赖

1. 确保已安装Python3（已在Python3.8.10上测试）。
2. 克隆或下载本项目。
3. 在项目目录中运行`pip install -r requirements.txt`安装依赖。

## 使用方法

1. 从手机端导出数据文件：
    1. 进入`Android/data/com.jiongji.andriod.card/files/baicizhan`目录。
    2. 将`baicizhantopicproblem.db`（包含已背的单词）和`lookup.db`（包含所有单词）导出到电脑。
2. 在电脑上运行`main.py`，按提示操作。

## 鸣谢

本项目参考了以下项目：

- [BaiCiZhanRememberedToExcel](https://github.com/tyza66/BaiCiZhanRememberedToExcel)

# README-en

BaiCiZhanPrinter is a tool that allows you to export the list of words you've learned from the BaiCiZhan mobile app.

## Features

- Supports exporting to `xlsx` or `html` format files. The `html` file can be further converted to `pdf` in a browser.
- Provides two export templates: **default template and dictation template**. The dictation template supports specifying the number of blank columns.
- Supports two sorting methods: **alphabetical order and random**.

## Installation

1. Ensure Python3 is installed (tested on Python3.8.10).
2. Clone or download this project.
3. Run `pip install -r requirements.txt` in the project directory to install dependencies.

## Usage

1. Export data files from the mobile side:
    1. Go to the `Android/data/com.jiongji.andriod.card/files/baicizhan` directory.
    2. Export `baicizhantopicproblem.db` (contains the words you've learned) and `lookup.db` (contains all words) to your computer.
2. Run `main.py` on your computer and follow the prompts.

## Acknowledgements

This project was inspired by the following project:

- [BaiCiZhanRememberedToExcel](https://github.com/tyza66/BaiCiZhanRememberedToExcel)