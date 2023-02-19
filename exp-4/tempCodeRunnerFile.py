in__":
    with Session(engine) as session:
        articles = session.query(Article).filter(Article.article_id == 1).all()
        for article in articles:
            print(article.title)
            for author in articles.authors:
                print(author.username)