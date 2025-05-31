from azure.mgmt.resource import ResourceManagementClient

# リソースグループを作成する関数
def create_resource_group(credential, subscription_id: str, location: str, resource_group_name: str):
    # リソースグループを操作するためのクライアントを作成
    resource_client = ResourceManagementClient(credential, subscription_id)

    # リソースグループの作成または更新（すでに存在する場合は上書き）
    rg_result = resource_client.resource_groups.create_or_update(
        resource_group_name,          # 作成するリソースグループ名
        {"location": location}        # リソースグループを作成するリージョン（例: japaneast）
    )

    # 作成完了メッセージを出力
    print(f"リソースグループ名( '{rg_result.name}' )は、('{rg_result.location}'に作成されました。)")

    # 作成したリソースグループ情報を返す（今後使いたいときのため）
    return rg_result
