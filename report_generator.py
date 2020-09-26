import os
from docxtpl import DocxTemplate
import json
from datetime import date
class report_app:
    def __init__(self,name):
        self.name = name
        self.paths()
    def report(self,vuln_count,share_data,computer_os,ips,account,general_data):
        doc = DocxTemplate(os.path.join('data','smb_template','smb_template.docx'))
        data={
            "name":self.name,
            "year":date.today().year-1911,
            "month":date.today().month,
            'day': date.today().day,  
            "vuln_count":vuln_count,
            "share_data":share_data,
            "computer_os":computer_os,
            "ips":ips,
            "accounts":account,
            "general_data":general_data
    
        }
        doc.render(data)
        doc.save(os.path.join("data","report",self.name+"_smb_report.docx"))
        # for vuln in data['share_data']:
        #     print(vuln)
        datas = json.dumps(data)
        outputfile = "data2.json"
        with open(outputfile,'w')as file:
                file.write(datas)
        # print(data)

    def data_count(self,datas):
        ips = []
        computer_os = []
        account = {}
        os_count = {
            "Windows 10":0,
            "Windows 7":0,
            "Windows 8":0,
            "Windows XP":0,
            "Windows Server 2016":0,
            "Windows Server 2012 R2":0,
            "Windows Server 2008 R2":0,
            "Windows Server 2008":0
        }
        general_data = {
            "account":0,
            "share_data":0,
            "vuln":{},
            
        }
        vuln_count = {
        }
        cve_2020_1206 = {
                "number":0,
                "ips":[],
                "description":"該漏洞產生的原因是SMB的解壓縮函數Srv2DecompressData在處理發送給目標SMBv3服務器以偽造的息請求時，所產生問題，攻擊者可以讀取未初始化的kernel內存，還可以對壓縮函數進行修改。",
                "solution":'用管理員身份執行命令提示字元，必輸入以下命令，Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" DisableCompression -Type DWORD -Value 1 -Force,此外無需重啟電腦',
                }
        cve_2020_0796 = {
                "number":0,
                "ips":[],
                "description":"該漏洞遠讓遠端攻擊者可對目標系統之SMBv3服務發送特製請求或架設惡意的SMBv3伺服器誘騙受害者進行連線，導致遠端執行任意程式碼",
                "solution":"目前微軟官方已針對此弱點釋出更新程式，請至下列連結進行更新：https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0796",
                }
        ms07_029 = {
                "number":0,
                "ips":[],
                "description":"ms07-029是一個遠程執行代碼漏洞，成功利用此漏洞的攻擊者可以遠程完全控制受影響的系統。攻擊者極有可能會可能查看、更改或刪除數據，或者創建擁有完全用戶權限的新帳戶。",
                "solution":"可從 Microsoft Update 取得此更新。開啟自動更新時，會自動下載和安裝此更新。",

            }
        ms08_067 = {
            "number":0,
            "ips":[],
            "description":"攻擊者弱成功利用此弱點，即可能造成使用者電腦受駭。其中TSPY_GIMMIV.A 惡意程式可能會下載WORM_GIMMIV.A 蠕蟲，並針對此弱點進行攻擊，而造成使用者系統受駭，導致用戶的帳號密碼、系統資訊等機敏性資料外洩，並可能造成受駭主機的防毒軟體無法執行、運作不正常",
            "solution":"相關解決方法，請輸入以下網址，https://blog.xuite.net/antivirus/hisecure/23147429-Conficker+%E8%A0%95%E8%9F%B2%E5%88%A9%E7%94%A8%E5%BE%AE%E8%BB%9FMS08-067+%E5%BC%B1%E9%BB%9E%E9%80%B2%E8%A1%8C%E6%94%BB%E6%93%8A%E4%B8%A6%E9%80%8F%E9%81%8E%E7%B6%B2%E8%B7%AF%E9%80%B2%E8%A1%8C%E6%93%B4%E6%95%A3%EF%BC%81",

        }
        ms10_054 = {
            "number":0,
            "ips":[],
            "description":"這個資訊安全更新可解決 Microsoft Windows 中數個未公開報告的弱點。 如果攻擊者蓄意製作 SMB 封包並將其傳送至受影響的系統，最嚴重的弱點可能會允許遠端執行程式碼。 最佳做法的防火牆和標準預設防火牆設定有助於防止網路受到來自企業外試圖利用這些弱點的攻擊。對於所有受支援版本的 Windows XP，此資訊安全更新的等級為「重大」。對於所有受支援版本的 Windows Server 2003、Windows Vista、Windows Server 2008、Windows 7 及 Windows Server 2008 R2，此資訊安全更新的等級為「重要」。這個資訊安全更新可修正 SMB 驗證 SMB 要求的方式，進而解決這些弱點。",
            "solution":" 大部分客戶都已啟用自動更新，並且不必須採取任何行動，因為資訊安全更新將自動下載和安裝。 沒有啟用自動更新的客戶則必須檢查更新，並手動安裝更新。",

        }
        ms10_061 = {
            "number":0,
            "ips":[],
            "description":"這個資訊安全更新可解決列印多工緩衝處理器服務中一項公開報告的資訊安全風險。 如果攻擊者將蓄意製作的列印要求傳送至具有曝露於 RPC 之列印多工緩衝處理器介面的受影響系統，此資訊安全風險可能會允許遠端執行程式碼。 依照預設，印表機目前不會於任何支援的 Windows 作業系統上進行共用。對於所有受支援版本的 Windows XP，此資訊安全更新的等級為「重大」。對於所有受支援版本的 Windows Server 2003、Windows Vista、Windows Server 2008、Windows 7 及 Windows Server 2008 R2，此資訊安全更新的等級為「重要」。此資訊安全更新可修正 Printer Spooler 服務驗證使用者權限的方式，藉以解決此資訊安全風險。",
            "solution":"大部分客戶都已啟用自動更新，並且不必須採取任何行動，因為資訊安全更新將自動下載和安裝。 沒有啟用自動更新的客戶則必須檢查更新，並手動安裝更新。 如需有關自動更新中特定設定選項的資訊，請參閱 Microsoft 知識庫文件編號 294871,https://support.microsoft.com/en-us/help/294871/description-of-the-automatic-updates-feature-in-windows。",  
        }
        ms17_010 = {
            "number":0,
            "ips":[],
            "description":"Microsoft Server Message Block 1.0 (SMBv1) 處理特定要求的方式中存在資訊洩漏弱點。攻擊者可能會蓄意製作封包，藉此導致伺服器資訊洩漏，以及執行任意程式。例如：WanaCrypt的勒索病毒，主要透過此弱點將受感染的電腦,大量檔案加密，並且要求高價比特幣贖金來贖回資料。",
            "solution":"關閉SMB1服務，詳細操作資訊，請到以下網址，https://walker-a.com/archives/4261，Step2開始將指引您如何關閉SMB1",
        }
        share_data = {}
        for data in datas:
            file = open(data)
            data = json.load(file)
            ips.append(data['ip'])
            computer_os.append(data['os'])

            if data["cve_2020_1206"] == "Vulnerable":
                cve_2020_1206["number"] += 1
                cve_2020_1206["ips"].append(data['ip'])
                vuln_count.update({"cve_2020_1206":cve_2020_1206})
            if data["cve_2020_0796"] == "Vulnerable":
                cve_2020_0796["number"] += 1
                cve_2020_0796["ips"].append(data['ip'])
                vuln_count.update({"cve_2020_0796":cve_2020_0796})
            if data["ms07-029"] == "Vulnerable":
                ms07_029["number"] += 1
                ms07_029["ips"].append(data['ip'])
                vuln_count.update({"ms07_029":ms07_029})
            if data["ms08-067"] == "Vulnerable":
                ms08_067["number"] += 1
                ms08_067["ips"].append(data['ip'])
                vuln_count.update({"ms08_067":ms08_067})
            if data["ms10-054"] == "Vulnerable":
                ms10_054["number"] += 1
                ms10_054["ips"].append(data['ip'])
                vuln_count.update({"ms10_054":ms10_054})
            if data["ms10-061"] == "Vulnerable":
                ms10_061["number"] += 1
                ms10_061["ips"].append(data['ip'])
                vuln_count.update({"ms10_061":ms10_061})
            if data["ms17-010"] == "Vulnerable":
                ms17_010["number"] += 1
                ms17_010["ips"].append(data['ip'])
                vuln_count.update({"ms17_010":ms17_010})                                                
            if data['password'] != "NULL" and data['account'] != "NULL":
                general_data['account'] += 1
                account.update({data['ip']:{"account":data["account"],"password":data["password"]}})
            if data['share_data'] != "NULL":
                general_data['share_data']+=1
                share_data.update({data['ip']:data["share_data"]})
        for vuln in vuln_count:
            temp_data = {
                vuln:vuln_count[vuln]['number']
            }
            general_data['vuln'].update(temp_data)
        self.report(vuln_count,share_data,computer_os,ips,account,general_data)
    # def cve_infomation(self,cve_name):
    #     description ={
    #         "cve_2020_1206":{
    #             "description":"該漏洞產生的原因是SMB的解壓縮函數Srv2DecompressData在處理發送給目標SMBv3服務器以偽造的息請求時，所產生問題，攻擊者可以讀取未初始化的kernel內存，還可以對壓縮函數進行修改。",
    #             "solution":'用管理員身份執行命令提示字元，必輸入以下命令，Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" DisableCompression -Type DWORD -Value 1 -Force,此外無需重啟電腦',
    #         },
    #         "cve_2020_0796":{
    #             "description":"該漏洞遠讓遠端攻擊者可對目標系統之SMBv3服務發送特製請求或架設惡意的SMBv3伺服器誘騙受害者進行連線，導致遠端執行任意程式碼",
    #             "solution":"目前微軟官方已針對此弱點釋出更新程式，請至下列連結進行更新：https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0796",
    #         },
    #         "ms08-067":{
    #             "description":"攻擊者弱成功利用此弱點，即可能造成使用者電腦受駭。其中TSPY_GIMMIV.A 惡意程式可能會下載WORM_GIMMIV.A 蠕蟲，並針對此弱點進行攻擊，而造成使用者系統受駭，導致用戶的帳號密碼、系統資訊等機敏性資料外洩，並可能造成受駭主機的防毒軟體無法執行、運作不正常",
    #             "solution":"相關解決方法，請輸入以下網址，https://blog.xuite.net/antivirus/hisecure/23147429-Conficker+%E8%A0%95%E8%9F%B2%E5%88%A9%E7%94%A8%E5%BE%AE%E8%BB%9FMS08-067+%E5%BC%B1%E9%BB%9E%E9%80%B2%E8%A1%8C%E6%94%BB%E6%93%8A%E4%B8%A6%E9%80%8F%E9%81%8E%E7%B6%B2%E8%B7%AF%E9%80%B2%E8%A1%8C%E6%93%B4%E6%95%A3%EF%BC%81",
    #         },
    #         "ms10-054":{
    #             "description":"這個資訊安全更新可解決 Microsoft Windows 中數個未公開報告的弱點。 如果攻擊者蓄意製作 SMB 封包並將其傳送至受影響的系統，最嚴重的弱點可能會允許遠端執行程式碼。 最佳做法的防火牆和標準預設防火牆設定有助於防止網路受到來自企業外試圖利用這些弱點的攻擊。對於所有受支援版本的 Windows XP，此資訊安全更新的等級為「重大」。對於所有受支援版本的 Windows Server 2003、Windows Vista、Windows Server 2008、Windows 7 及 Windows Server 2008 R2，此資訊安全更新的等級為「重要」。這個資訊安全更新可修正 SMB 驗證 SMB 要求的方式，進而解決這些弱點。",
    #             "solution":" 大部分客戶都已啟用自動更新，並且不必須採取任何行動，因為資訊安全更新將自動下載和安裝。 沒有啟用自動更新的客戶則必須檢查更新，並手動安裝更新。",
    #         },        
    #         "ms10-061":{
    #             "description":"這個資訊安全更新可解決列印多工緩衝處理器服務中一項公開報告的資訊安全風險。 如果攻擊者將蓄意製作的列印要求傳送至具有曝露於 RPC 之列印多工緩衝處理器介面的受影響系統，此資訊安全風險可能會允許遠端執行程式碼。 依照預設，印表機目前不會於任何支援的 Windows 作業系統上進行共用。對於所有受支援版本的 Windows XP，此資訊安全更新的等級為「重大」。對於所有受支援版本的 Windows Server 2003、Windows Vista、Windows Server 2008、Windows 7 及 Windows Server 2008 R2，此資訊安全更新的等級為「重要」。此資訊安全更新可修正 Printer Spooler 服務驗證使用者權限的方式，藉以解決此資訊安全風險。",
    #             "solution":"大部分客戶都已啟用自動更新，並且不必須採取任何行動，因為資訊安全更新將自動下載和安裝。 沒有啟用自動更新的客戶則必須檢查更新，並手動安裝更新。 如需有關自動更新中特定設定選項的資訊，請參閱 Microsoft 知識庫文件編號 294871,https://support.microsoft.com/en-us/help/294871/description-of-the-automatic-updates-feature-in-windows。",
    #         },
    #         "ms17-010":{
    #             "description":"Microsoft Server Message Block 1.0 (SMBv1) 處理特定要求的方式中存在資訊洩漏弱點。攻擊者可能會蓄意製作封包，藉此導致伺服器資訊洩漏，以及執行任意程式。例如：WanaCrypt的勒索病毒，主要透過此弱點將受感染的電腦,大量檔案加密，並且要求高價比特幣贖金來贖回資料。",
    #             "solution":"關閉SMB1服務，詳細操作資訊，請到以下網址，https://walker-a.com/archives/4261，Step2開始將指引您如何關閉SMB1",
    #         },
            
    #     }
    #     return description[cve_name]['description'],description[cve_name]["solution"]
    def paths(self):
    
        path = os.path.join('data','clean_data')
        files = os.listdir(path)
        files = [os.path.join(path,file) for file in files]
        self.data_count(files)

if __name__ == "__main__":
    report_app("衛生福利部109年資通安全稽核作業")
