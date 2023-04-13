import Extract
import Transform
import Load

def main():
    url = "https://fortlauderdale.data.socrata.com/resource/4han-ff9s.csv"
    db_path = 'vandalism.db'
    df = Extract.extract_data(url)
    df = Transform.transform_data(df)
    Load.load_data(df, db_path)


if __name__ == '__main__':
    main()
