# Daily Sentences

## Introduction
This program was conceived at the end of 2024, with the idea to digitize my cherished collection that has accompanied me for nearly six years, documenting all my journeys. This compilation contains over 3000 sentences. Midway through this project, I thought, could I create a program that randomly showcases these sentences in front of me, similar to those daily sentence recommendation apps? Thus began this half-year-long endeavor filled with numerous challenges and bugs. With just one Python course from school under my belt before starting on this project, I encountered many difficulties initially, such as choosing a UI library and learning frontend languages - all completely new to me. However, when I first showed my roommate the not-yet-complete interface, I was genuinely happy. Happy that my beloved collection found a new way to accompany me on my computer, and happy that my learning finally bore fruit (being able to implement small ideas from my head using programming languages is truly a wonderful thing). Over these six months, I have indeed learned a lot, and although this first version of the program still has its imperfections, as a gift to myself for my 20th birthday, it has made me immensely happy. It’s a program of great personal significance.
Disclaimer: All sentences are sourced from my collection, taken from the internet and various books. Please contact me if there are any copyright issues.

## Core Features

### 1. Sentence Display and Management
- **Random Sentence Display**: Upon launching the application, a sentence is randomly selected from my collection for display.
- **Sentence Search**: Users can input keywords into the search box to find specific sentences. If matches are found, the first matching sentence will be displayed, allowing users to browse other results via "Previous" and "Next" buttons.
- **Favorite Function**: Clicking the favorite button marks sentences liked by the user, adding them to a favorites list for easy access later. There is also functionality to switch between the main page and the favorites page.

### 2. Music Playback
- **Music File Selection**: Supports users specifying a folder containing MP3 files as a music library. Once selected, all qualifying audio files will be automatically loaded into the playlist. You can click on the area displaying the music name to trigger the selection of the music path or add your music files to the `./resources/music` folder for default playback.
- **Playback Control**: Provides basic control buttons like play/pause, previous track, next track, making it easy for users to control the music playback process.
- **Progress Bar**: Displays the current song's playback progress and allows users to drag the slider to quickly jump to any position.
- **Auto-play**: When a song ends, the system automatically starts playing the next song in the playlist.

### 3. User Interface
- **Mouse Hover Halo**: In the text box where sentences are displayed, a halo effect that changes color over time follows your mouse.

### 4. Shortcut Keys Support
To improve user operation efficiency, the app supports a series of shortcut key operations such as play/pause music, switching songs, etc.
- Space: Favorite or unfavorite the current sentence.
- Ctrl + Space: Play or pause the current music.
- Left Arrow Key: Switch to the previous sentence.
- Right Arrow Key: Switch to the next sentence.
- Alt: Toggle between the main page (displaying random sentences) and the favorites page.
- Ctrl + Left Arrow Key: Skip to the previous song.
- Ctrl + Right Arrow Key: Skip to the next song.

### 5. Main Components
- **Date Display**: Shows the current month and date.
- **Search Box**: Enter keywords to find specific sentences.
- **Text Box**: Displays random or search result sentences, featuring a mouse hover halo effect.
- **Favorite Button**: Add the current sentence to favorites.
- **Music Playback Controls**: Includes play/pause buttons, previous track, next track buttons, and a progress bar, supporting shortcut key operations.

## Contribution
I welcome contributions from community members, whether proposing new features, reporting bugs, or submitting code improvements. Please follow the standard Git workflow for contributions.


# 每日句子

## 简介
这个程序诞生于2024年年底的一个想法，将陪伴我将近6年之久的，像记录我所有来路的摘抄本“电子化”，从而方便我查找其中的3000多个句子。这项工作进行到一半的时候，我想，我是不是可以写一个程序，将这些句子随机展现在我眼前，就像那些日推句子的软件一样？于是这项长达半年之久工作就正式开始了，伴随着许多的困难和bug。从我刚刚学习编程到开始写这个程序之间大概只有学校的一门Python课，所以一开始的我遇到了许多困难，构建界面库的选择，前端语言的学习等，这些都是我第一次接触的。但是当我第一次给室友展示那个功能也许还不完整的界面的时候，我真的很开心。我开心于自己珍爱的摘抄本得以用另一个方式在电脑上陪伴我，也开心于自己的学习终于有了反馈（能用编程语言实现自己脑子里一个个小小的想法真的是一件很棒的事情）。这半年以来，我也确实学习到了很多东西，尽管要发布的这个第一版程序仍然有些不尽如人意的地方，但是作为送给自己的20岁生日礼物，它真的已经让我足够开心，它是一个对我而言如此有特殊纪念意义的程序。
声明：所有句子均是我的摘抄本上的句子，摘自网络以及各类书籍，如有侵权请联系我。

## 核心功能

### 1. 句子展示与管理
- **随机句子展示**: 应用启动时，会从我的摘抄本句子库中随机选取一条语句进行展示。
- **句子搜索**: 用户可以通过搜索框输入关键词来查找特定的句子。如果找到匹配项，则会显示第一条匹配的句子，并允许用户通过“上一句”、“下一句”按钮查看其他结果。
- **收藏功能**: 用户可以点击收藏按钮来标记喜欢的句子。这些句子会被添加到收藏夹中，方便日后查阅。同时，提供了在主页面和收藏夹之间切换的功能。

### 2. 音乐播放
- **音乐文件选择**: 支持用户指定包含MP3文件的文件夹作为音乐库。一旦选定，所有符合条件的音频文件将被自动加载到播放列表中。你可以点击显示音乐名称的区域来触发对于音乐路径的选择，也可以将你的音乐文件加入目录下的./resources/music文件夹以默认播放。
- **播放控制**: 提供了播放/暂停、上一首、下一首等基本控制按钮，让用户能够轻松地控制音乐播放流程。
- **进度条**: 显示当前歌曲的播放进度，并允许用户拖动滑块快速跳转至任意位置。
- **自动播放**: 当一首歌结束时，系统会自动开始播放列表中的下一首歌曲。

### 3. 用户界面
- **鼠标悬停光晕**: 在句子显示的文本框中，会随时间变化颜色的光晕将跟随你的鼠标。

### 4. 快捷键支持
为了提高用户的操作效率，该应用还支持一系列快捷键操作，如播放/暂停音乐、切换歌曲等。
空格: 收藏或取消收藏当前句子。
Ctrl + 空格: 播放或暂停当前音乐。
左箭头键: 切换到上一个句子。
右箭头键: 切换到下一个句子。
Alt: 在主页面（显示随机句子）和收藏夹页面之间切换。
Ctrl + 左箭头键: 切换到上一首歌。
Ctrl + 右箭头键: 切换到下一首歌。

### 5. 主要组件
日期显示: 显示当前月份和日期。
搜索框: 输入关键词以查找特定句子。
文本框: 展示随机或搜索结果中的句子，带有鼠标悬停光晕效果。
收藏按钮: 收藏当前句子到收藏夹。
音乐播放控制: 包括播放/暂停按钮、上一首、下一首按钮及进度条，支持快捷键操作。

## 贡献
我欢迎社区成员为这个项目做出贡献，无论是提出新功能建议、报告bug还是提交代码改进。请遵循标准的Git工作流程进行贡献。
