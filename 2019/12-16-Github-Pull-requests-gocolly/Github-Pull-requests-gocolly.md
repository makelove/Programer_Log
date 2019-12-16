- 使用gocolly爬虫，想统计抓取情况发现不方便，所以自己修改colly.go写了一个方法Statistics
    - https://github.com/gocolly/colly/issues/411
- 参考
    - [git学习--GitHub上如何进行PR(Pull Request)操作](https://blog.csdn.net/qq_33429968/article/details/62219783)    
    
- PR步骤
```shell script
#首先fork gocolly 到自己的GitHub

# 然后clone到本地
(.py3) pro:github play$ mkdir PR
(.py3) pro:github play$ cd PR
(.py3) pro:PR play$ git clone git@github.com:makelove/colly.git
Cloning into 'colly'...
remote: Enumerating objects: 130, done.
remote: Counting objects: 100% (130/130), done.
remote: Compressing objects: 100% (97/97), done.
remote: Total 1797 (delta 33), reused 52 (delta 8), pack-reused 1667
Receiving objects: 100% (1797/1797), 8.16 MiB | 43.00 KiB/s, done.
Resolving deltas: 100% (955/955), done.
(.py3) pro:PR play$
(.py3) pro:PR play$ ls
.     ..    colly
(.py3) pro:PR play$ cd colly/

#与 https://github.com/gocolly/colly 建立链接
(.py3) pro:colly play$ git remote -v
origin	git@github.com:makelove/colly.git (fetch)
origin	git@github.com:makelove/colly.git (push)
(.py3) pro:colly play$ git remote add upstream https://github.com/gocolly/colly.git
(.py3) pro:colly play$ git remote -v
origin	git@github.com:makelove/colly.git (fetch)
origin	git@github.com:makelove/colly.git (push)
upstream	https://github.com/gocolly/colly.git (fetch)
upstream	https://github.com/gocolly/colly.git (push)

#建立分支
(.py3) pro:colly play$ git branch
* master
(.py3) pro:colly play$ git checkout -b  Statistics
Switched to a new branch 'Statistics'
(.py3) pro:colly play$ git branch
* Statistics
  master
#修改代码
(.py3) pro:colly play$ sub .

#提交代码
(.py3) pro:colly play$ git status
On branch Statistics
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   colly.go

no changes added to commit (use "git add" and/or "git commit -a")
(.py3) pro:colly play$ git add colly.go
(.py3) pro:colly play$ git commit -m "add Statistics function to colly.Collector"
[Statistics fe0f649] add Statistics function to colly.Collector
 1 file changed, 12 insertions(+)
(.py3) pro:colly play$ git status
On branch Statistics
nothing to commit, working tree clean
(.py3) pro:colly play$ git push
fatal: The current branch Statistics has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin Statistics

(.py3) pro:colly play$ git push --set-upstream origin Statistics
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 466 bytes | 466.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'Statistics' on GitHub by visiting:
remote:      https://github.com/makelove/colly/pull/new/Statistics
remote:
To github.com:makelove/colly.git
 * [new branch]      Statistics -> Statistics
Branch 'Statistics' set up to track remote branch 'Statistics' from 'origin'.
```    

- 在https://github.com/makelove/colly/pulls 创建  Pull requests 
    - 检查代码
    - 提交