from src.database.client import get_supabase_client

def main():
    supabase=get_supabase_client()
    response=(supabase.table("cusomers")
    .select("id","full_name","email")
    .limit(5)
    .execute())
    print("Supabase connection successful!")
    print(response.data)

if __name__=="__main__":
    main()