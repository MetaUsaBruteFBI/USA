if __name__ == "__main__":
	try:
		__import__("enc_bug").make()
	except Exception as e:
		exit(str(e))
