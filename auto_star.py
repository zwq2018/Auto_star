import requests
import re



def extract_github_urls(input_text):
    return re.findall(r"https://github\.com/[^/]+/[^/\s]+", input_text)


def parse(url):
    match = re.match(r"https://github\.com/([^/]+)/([^/]+)", url)
    if match:
        owner, repo = match.groups()
    else:
        owner, repo = None, None
    return owner, repo

def star_github_repo(token, owner, repo):
    """
    Star a GitHub repository using the GitHub API.

    :param token: Your personal GitHub token.
    :param owner: The owner of the repo you want to star.
    :param repo: The name of the repo you want to star.
    """
    url = f"https://api.github.com/user/starred/{owner}/{repo}"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.put(url, headers=headers)

    if response.status_code == 204:
        print(f"Successfully starred {owner}/{repo}!")
    else:
        print(
            f"Failed to star {owner}/{repo}. Response code: {response.status_code}, Response message: {response.text}")

# Replace 'YOUR_GITHUB_TOKEN' with your actual token
urls='''
1. https://github.com/MarSaKi/VLN-BEVBert
2. https://github.com/Shilin-LU/TF-ICON
3. https://github.com/HCPLab-SYSU/CausalVLR
4. https://github.com/FeiElysia/ViECap
5. https://github.com/OwXiaoM/PCS
6. https://github.com/Adamdad/DeRy
7. https://github.com/miaoyuchun/DDS2M
8. https://github.com/Qinying-Liu/CASE
9. https://github.com/yyvhang/IAGNet
10. https://github.com/alibaba-damo-academy/alice/tree/main
11. https://github.com/NJUyued/PRG4SSL-MNAR
12. https://github.com/TongkunGuan/CCD
13. https://github.com/TrepangCat/3D_Semantic_Subspace_Traverser
14. https://github.com/DZhaoXd/DT-ST/tree/main
15. https://github.com/Tianhao-Qi/BACL
16. https://github.com/MarSaKi/ETPNav
17. https://github.com/haoni0812/MDA
18. https://github.com/CuiRuikai/Partial2Complete
19. https://github.com/IMCCretrieval/ProST
20. https://github.com/PRIS-CV/On-the-fly-Category-Discovery
21. https://github.com/miaoyuchun/DS2DP
22. https://github.com/showlab/UniVTG
23. https://github.com/Yanfeng-Zhou/SPC
24. https://github.com/Yanfeng-Zhou/XNet
25. https://github.com/RaymondWang987/NVDS
26. https://github.com/jiaxiZeng/Parameterized-Cost-Volume-for-Stereo-Matching
27. https://github.com/zwq2018/Data-Copilot
28. https://github.com/Yujianyuan/Exp-BLIP
29. https://github.com/wl-zhao/VPD
30. https://github.com/awei669/VQ-Font
31. https://github.com/bollossom/ICLR_TINY_SNN
32. https://github.com/bollossom/GAC
33. https://github.com/NJUyued/MutexMatch4SSL
34. https://github.com/Sense-X/HoP
35. https://github.com/Sense-X/Co-DETR
36. https://github.com/PJLab-ADG/LoGoNet
37. https://github.com/haoyuc/MaskedDenoising
38. https://github.com/haoyuc/VideoDesnowing
39. https://github.com/mechsihao/FaissSearcher
40. https://github.com/mechsihao/RecommendFlow
41. https://github.com/TongkunGuan/SIGA
42. https://github.com/jinyeying/night-enhancement
43. https://github.com/scott-yjyang/ViWS-Net
44. https://github.com/scott-yjyang/DiffMIC
45. https://github.com/jinyeying/DC-ShadowNet-Hard-and-Soft-Shadow-Removal
'''
urls_list = extract_github_urls(urls)
token = ''  # your github token


for i in range(len(urls_list)):
    url = urls_list[i]
    owner, repo = parse(url)
    star_github_repo(token, owner, repo)

