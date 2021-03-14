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

2021.03.07
・windows exeファイルを作ろうとしたけど、
　作れない。
・setup.pyでコマンドラインツールとして作成する方針に変更
