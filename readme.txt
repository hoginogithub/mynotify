2021.03.14
・コマンドラインツールとして作り直し
・C:\Users\hogin\AppData\Local\Programs\Python\Python38\python.exeで仮想環境venvを作成
　C:\Users\hogin\AppData\Local\Programs\Python\Python38\python.exe　-m venv venv
・仮想環境用のプロンプトを起動するバッチファイルを作成し起動
　startproject.bat
・仮想環境にインストールしたパケージ
　plyer
　Click
・エディタでrequirements.txtを作成
・requirements.lockを作成
　pip freeze > requirements.lock
・仮想環境のpython.exe
　C:\Users\hogin\Documents\prog\python\windowsapp\notification2\venv\Scripts\python.exe
・github
  https://github.com/hoginogithub/mynotify.git
・circlci
  githubのアカウントを使用
  https://app.circleci.com/projects/project-setup/github/hoginogithub/notification
・setup.pyを作成して実行
　pip install -e .

2021.03.07
・windows exeファイルを作ろうとしたけど、
　作れない。
・setup.pyでコマンドラインツールとして作成する方針に変更
