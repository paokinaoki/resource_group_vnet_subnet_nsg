

from config import SUBSCRIPTION_ID, LOCATION, RESOURCE_GROUP_NAME

from azure.identity import DefaultAzureCredential

from resource_group import create_resource_group
from vnet import create_vnet
from subnet import create_subnet
from nsg import create_nsg


def main():
    """
    mainの処理、
    Resource Group & VNET & Subnet & NSG
        args1: args1の説明を書いてね
            EX) 例
        args2: args2の説明を書いてね
            Ex) 例
    Return 戻り値の説明
        ret_val: ret_valの説明を書いてね
    Raises: 発砲するエラーの説明
        ※try/exceptを使用するときのみ
    TODO:
        - まだできていないけどやりたいことを書いてね。
    """

    # 認証処理
    credential = DefaultAzureCredential()

    # リソースグループを作成
    create_resource_group(credential,SUBSCRIPTION_ID, LOCATION, RESOURCE_GROUP_NAME)

    # 他のリソース作成処理
    # create_vnet(credential, subscription_id, location, vnet_name)
    # create_subnet(credential, subscription_id, location, subnet_name)
    # create_nsg(credential, subscription_id, location, nsg_name)

if __name__ == "__main__":
    main()
