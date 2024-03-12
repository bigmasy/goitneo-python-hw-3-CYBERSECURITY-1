Застосунок "Адресна книга"
=======

Вимоги
----------
None

Перелік функцій застосунка
-----------
None

Правила розробки
-----------
Використання git
1) Головна гілка репозиторія називається main. Для кожної задачі створюється нова гілка скопійована з головної. Для назви гілки використовуйте код вказаний в назві задачі.
Приклад результату виконання команд в git: 
```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```
```
$ git checkout -b RAB-10
Switched to a new branch 'RAB-10'
```
2) При збережені задач в репозиторії використовуйте коротке речення яке опише дії які ви збираєтесь зберегти.
Приклад результату виконання команд в git: 
```
$ git status
On branch RAB-10
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
```
$ git add .
```
```
$ git commit -m "RAB-10: правило роботи з git"
[RAB-10 431b1f8] RAB-10: правило роботи з git
 1 file changed, 16 insertions(+), 2 deletions(-)
```
3) Перед відправленням змін на сервер треба впевнитися, що гілка задачі сумісна з найсвежішою версією гілки main
```
$ git fetch
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 965 bytes | 965.00 KiB/s, done.
From github.com:aaleksieiev/goitneo-python-final-CYBERSECURITY-1
   4308d5e..2be7f29  main       -> origin/main
```
```
$ git merge origin main
Auto-merging README.md
Merge made by the 'ort' strategy.
 README.md | 2 --
 1 file changed, 2 deletions(-)
```
```
$git push origin RAB-10
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.19 KiB | 1.19 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
remote: 
remote: Create a pull request for 'RAB-10' on GitHub by visiting:
remote:      https://github.com/aaleksieiev/goitneo-python-final-CYBERSECURITY-1/pull/new/RAB-10
remote: 
To github.com:aaleksieiev/goitneo-python-final-CYBERSECURITY-1.git
 * [new branch]      RAB-10 -> RAB-10
```