import os
import sys

def run_bisect(bad_commit, good_commit):
    os.system(f"git bisect start {bad_commit} {good_commit}")
    
    exit_code = os.system("git bisect run python manage.py test")
    
    if exit_code == 0:
        print("Le commit responsable du bug a été identifié.")
    else:
        print("Erreur lors de l'exécution du bisect.")
    
    os.system("git bisect reset")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python myscript.py <bad_commit> <good_commit>")
        sys.exit(1)
    
    bad_commit = sys.argv[1]
    good_commit = sys.argv[2]
    
    run_bisect(bad_commit, good_commit)
