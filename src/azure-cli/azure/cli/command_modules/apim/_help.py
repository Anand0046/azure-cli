# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#
# Generation mode: Incremental
# --------------------------------------------------------------------------
from .generated._help import helps  # pylint: disable=reimported
try:
    from .manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['apim'] = """
type: group
short-summary: Manage Azure API Management services.
"""

helps['apim api'] = """
type: group
short-summary: Manage Azure API Management API's.
"""

helps['apim product api'] = """
type: group
short-summary: Manage Azure API Management Product's APIs.
"""

helps['apim product'] = """
type: group
short-summary: Manage Azure API Management Product's.
"""

helps['apim nv'] = """
type: group
short-summary: Manage Azure API Management Named Values.
"""

helps['apim api operation'] = """
type: group
short-summary: Manage Azure API Management API Operations.
"""

helps['apim api release'] = """
type: group
short-summary: Manage Azure API Management API Release.
"""

helps['apim api revision'] = """
type: group
short-summary: Manage Azure API Management API Revision.
"""

helps['apim api versionset'] = """
type: group
short-summary: Manage Azure API Management API Version Set.
"""

helps['apim api schema'] = """
type: group
short-summary: Manage Azure API Management API Schema's.
"""

helps['apim deletedservice'] = """
type: group
short-summary: Manage soft-deleted Azure API Management services.
"""

helps['apim backup'] = """
type: command
short-summary: Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.
examples:
  - name: Create a backup of the API Management service instance
    text: |-
        az apim backup --name MyApim -g MyResourceGroup --backup-name myBackup \
             --storage-account-name mystorageaccount --storage-account-container backups \
             --storage-account-key Ay2ZbdxLnD4OJPT29F6jLPkB6KynOzx85YCObhrw==
"""

helps['apim restore'] = """
type: command
short-summary: Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete.
examples:
  - name: Restores a backup of the API Management service instance
    text: |-
        az apim restore --name MyApim -g MyResourceGroup --backup-name myBackup \
             --storage-account-name mystorageaccount --storage-account-container backups \
             --storage-account-key Ay2ZbdxLnD4OJPT29F6jLPkB6KynOzx85YCObhrw==
"""

helps['apim apply-network-updates'] = """
type: command
short-summary: Update the API Management resource running in the virtual network to pick the updated network settings.
examples:
  - name: Update the virtual network settings of the API Management service instance
    text: |-
        az apim apply-network-updates --name MyApim -g MyResourceGroup
"""

helps['apim create'] = """
type: command
short-summary: Create an API Management service instance.
parameters:
  - name: --name -n
    type: string
    short-summary: unique name of the service instance to be created
    long-summary: |
        The name must be globally unique since it will be included as the gateway
        hostname like' https://my-api-servicename.azure-api.net'.  See examples.
examples:
  - name: Create a Developer tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --publisher-email email@mydomain.com --publisher-name Microsoft
  - name: Create a Consumption tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --sku-name Consumption --enable-client-certificate \\
            --publisher-email email@mydomain.com --publisher-name Microsoft
"""

helps['apim delete'] = """
type: command
short-summary: Deletes an API Management service.
examples:
  - name: Delete an API Management service.
    text: >
        az apim delete -n MyApim -g MyResourceGroup
"""

helps['apim list'] = """
type: command
short-summary: List API Management service instances.
"""

helps['apim show'] = """
type: command
short-summary: Show details of an API Management service instance.
"""

helps['apim update'] = """
type: command
short-summary: Update an API Management service instance.
"""

helps['apim wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of an apim is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a apim is met. (autogenerated)
    text: |
        az apim wait --created --name MyApim --resource-group MyResourceGroup
    crafted: true
"""

helps['apim api list'] = """
type: command
short-summary: List API Management API's.
"""

helps['apim api show'] = """
type: command
short-summary: Show details of an API Management API.
"""

helps['apim api delete'] = """
type: command
short-summary: Delete an API Management API.
"""

helps['apim api create'] = """
type: command
short-summary: Create an API Management API.
parameters:
  - name: --api-id
    type: string
    short-summary: unique name of the api to be created
    long-summary: |
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
  - name: --path
    type: string
    short-summary: Path to the API
  - name: --display-name
    type: string
    short-summary: Display name of the API to be created
examples:
  - name: Create a basic API.
    text: |-
        az apim api create --service-name MyApim -g MyResourceGroup --api-id MyApi --path '/myapi' --display-name 'My API'
"""

helps['apim api update'] = """
type: command
short-summary: Update an API Management API.
parameters:
  - name: --api-id
    type: string
    short-summary: unique name of the api to be created
    long-summary: |
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
examples:
  - name: Create a basic API.
    text: |-
        az apim api update --service-name MyApim -g MyResourceGroup --api-id MyApi --description foo
"""

helps['apim api wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of an apim api is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a apim api is met. (autogenerated)
    text: |
        az apim api wait --created --api-id MyApi --name MyApim --resource-group MyResourceGroup
    crafted: true
"""

helps['apim api import'] = """
type: command
short-summary: Import an API Management API.
examples:
  - name: Import an API Management API From a file or a url
    text: |-
        az apim api import -g MyResourceGroup --service-name MyApim --path MyApi --specification-url https://MySpecificationURL --specification-format OpenApiJson
"""

helps['apim product api list'] = """
type: command
short-summary: Lists a collection of the APIs associated with a product.
examples:
  - name: List all APIs associated with a product.
    text: |-
        az apim product api list --resource-group MyResourceGroup  --service-name MyServiceName  --product-id MyProductID
"""

helps['apim product api check'] = """
type: command
short-summary: Checks that API entity specified by identifier is associated with the Product entity.
examples:
  - name: Check if the API is associated with the Product.
    text: |-
        az apim product api check --resource-group MyResourceGroup  --service-name MyServiceName  --product-id MyProductID --api-id MyAPIID
"""

helps['apim product api add'] = """
type: command
short-summary: Add an API to the specified product.
examples:
  - name: Add an API to the specified product.
    text: |-
        az apim product api add --resource-group MyResourceGroup --service-name MyServiceName  --product-id MyProductID --api-id MyAPIID
"""

helps['apim product api delete'] = """
type: command
short-summary: Deletes the specified API from the specified product.
examples:
  - name: Deletes the specified API from the specified product.
    text: |-
        az apim product api delete --resource-group MyResourceGroup --service-name MyServiceName  --product-id MyProductID --api-id MyAPIID
"""

helps['apim product list'] = """
type: command
short-summary: Lists a collection of products in the specified service instance.
examples:
  - name: List all products for this APIM instance.
    text: |-
        az apim product list --resource-group MyResourceGroup --service-name MyServiceName
"""

helps['apim product show'] = """
type: command
short-summary: Gets the details of the product specified by its identifier.
examples:
  - name: Gets the details of the product specified by its identifier.
    text: |-
        az apim product show --resource-group MyResourceGroup --service-name MyServiceName  --product-id MyProductID
"""

helps['apim product create'] = """
type: command
short-summary: Creates a product.
examples:
  - name: Creates a product.
    text: |-
        az apim product create --resource-group MyResourceGroup  --service-name MyServiceName --product-id MyProductID --product-name MyProductName --description MyDescription --legal-terms MyTerms --subscription-required true --approval-required true --subscriptions-limit 8 --state "published"
"""

helps['apim product update'] = """
type: command
short-summary: Update existing product details.
examples:
  - name: Update existing product details.
    text: |-
        az apim product update --resource-group MyResourceGroup  --service-name MyServiceName --product-id MyProductID --product-name MyNewProductName --description MyNewDescription --legal-terms MyNewTerms --subscription-required false --state "notPublished"
"""

helps['apim product delete'] = """
type: command
short-summary: Delete product.
examples:
  - name: Delete product with all subscriptions to this product.
    text: |-
        az apim product delete --resource-group MyResourceGroup  --service-name MyServiceName --product-id MyProductID --delete-subscriptions true
"""

helps['apim product wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of an apim product is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a apim is met. (autogenerated)
    text: |
        az apim product wait --created --resource-group MyResourceGroup --service-name MyServiceName --product-id MyProductID
    crafted: true
"""

helps['apim nv list'] = """
type: command
short-summary: List API Management Named Values.
"""

helps['apim nv show'] = """
type: command
short-summary: Show details of an API Management Named Value.
"""

helps['apim nv show-secret'] = """
type: command
short-summary: Gets the secret of an API Management Named Value.
"""

helps['apim nv delete'] = """
type: command
short-summary: Delete an API Management Named Value.
"""

helps['apim nv create'] = """
type: command
short-summary: Create an API Management Named Value.
parameters:
  - name: --named-value-id
    type: string
    short-summary: unique name for the Named Value to be created
    long-summary: |
        Must be unique in the current API Management service instance.
  - name: --display-name
    type: string
    short-summary: The Display name of the Named Value.
  - name: --value
    type: string
    short-summary: The value of the Named Value.
examples:
  - name: Create a Named Value.
    text: |-
        az apim nv create --service-name MyApim -g MyResourceGroup --named-value-id MyNamedValue --display-name 'My Named Value' --value 'foo'
"""

helps['apim nv update'] = """
type: command
short-summary: Update an API Management Named Value.
parameters:
  - name: --named-value-id
    type: string
    short-summary: unique name of the api to be created
    long-summary: |
        Must be unique in the current API Management service instance.
  - name: --value
    type: string
    short-summary: The value of the Named Value.
examples:
  - name: Create a basic API.
    text: |-
        az apim nv update --service-name MyApim -g MyResourceGroup --named-value-id MyNamedValue --value foo
"""

helps['apim nv wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of an apim named value is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a apim api is met.
    text: |
        az apim nv wait --created --service-name MyApim -g MyResourceGroup --named-value-id MyNamedValue --resource-group MyResourceGroup
"""

helps['apim api operation list'] = """
type: command
short-summary: List a collection of the operations for the specified API.
examples:
  - name: List a collection of the operations for the specified API.
    text: |-
        az apim api operation list --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId
"""

helps['apim api operation show'] = """
type: command
short-summary: Gets the details of the API Operation specified by its identifier.
examples:
  - name: Gets the details of the API Operation specified by its identifier.
    text: |-
        az apim api operation show --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --operation-id MyOperationId
"""

helps['apim api operation create'] = """
type: command
short-summary: Creates a new operation in the API
examples:
  - name: Creates a new operation in the API with several parameters
    text: |-
        az apim api operation create --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --url-template "/session/{param1}/{param2}" --method "GET" --display-name MyOperationName --description MyDescription --template-parameters name=param1 description=descriptionContent type=paramType required="true" --template-parameters name=param2 required="false" type="string"
"""

helps['apim api operation update'] = """
type: command
short-summary: Updates the details of the operation in the API specified by its identifier.
examples:
  - name: Updates method, displayname, description of the operation in the API specified by its identifier.
    text: |-
        az apim api operation update --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --operation-id MyOperationId --method "PUT" --display-name NewDisplayName --description NewDescription
"""

helps['apim api operation delete'] = """
type: command
short-summary: Deletes the specified operation in the API.
examples:
  - name: Deletes the specified operation in the API.
    text: |-
        az apim api operation delete --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --operation-id MyOperationId
"""

helps['apim api release list'] = """
type: command
short-summary: Lists all releases of an API.
examples:
  - name: Lists all releases of an API.
    text: |-
        az apim api release list --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId
"""

helps['apim api release show'] = """
type: command
short-summary: Returns the details of an API release.
examples:
  - name: Returns the details of an API release.
    text: |-
        az apim api release show --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId
"""

helps['apim api release create'] = """
type: command
short-summary: Creates a new Release for the API.
examples:
  - name: Creates a new Release for the API.
    text: |-
        az apim api release create --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId --api-revision 2 --notes MyNotes
"""

helps['apim api release update'] = """
type: command
short-summary: Updates the details of the release of the API specified by its identifier.
examples:
  - name: Updates the notes of the release of the API specified by its identifier.
    text: |-
        az apim api release update --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId --notes MyNewNotes
"""

helps['apim api release delete'] = """
type: command
short-summary: Deletes the specified release in the API.
examples:
  - name: Deletes the specified release in the API.
    text: |-
        az apim api release delete --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId
"""

helps['apim api revision list'] = """
type: command
short-summary: Lists all revisions of an API.
examples:
  - name: Lists all revisions of an API.
    text: |-
        az apim api revision list --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId
"""

helps['apim api revision create'] = """
type: command
short-summary: Create API revision.
examples:
  - name: Create a revision for the specfic API.
    text: |-
        az apim api revision create --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --api-revision RevisionNumber --api-revision-description RevisionDescription
"""

helps['apim api versionset list'] = """
type: command
short-summary: Lists a collection of API Version Sets in the specified service instance.
examples:
  - name: Lists a collection of API Version Sets in the specified service instance.
    text: |-
        az apim api versionset list --resource-group MyResourceGroup --service-name MyServiceName
"""

helps['apim api versionset show'] = """
type: command
short-summary: Gets the details of the Api Version Set specified by its identifier.
examples:
  - name: Gets the details of the Api Version Set specified by its identifier.
    text: |-
        az apim api versionset show --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId
"""

helps['apim api versionset create'] = """
type: command
short-summary: Creates a Api Version Set.
examples:
  - name: Creates a Api Version Set with version schema as header.
    text: |-
        az apim api versionset create --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --display-name MyDisplayName --versioning-scheme "Header" --description MyDescription --version-header-name MyHeaderName
  - name: Creates a Api Version Set with version schema as query.
    text: |-
        az apim api versionset create --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --display-name MyDisplayName --versioning-scheme "Query" --description MyDescription --version-query-name MyQueryName
"""

helps['apim api versionset update'] = """
type: command
short-summary: Updates the details of the Api VersionSet specified by its identifier.
examples:
  - name: Updates the description, display-name of the Api VersionSet specified by its identifier.
    text: |-
        az apim api versionset update --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --display-name MyNewDisplayName --description MyNewDescription
  - name: Updates the version schema of the Api VersionSet specified by its identifier.
    text: |-
        az apim api versionset update --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --versioning-scheme "Query" --version-query-name MyNewQueryName
"""

helps['apim api versionset delete'] = """
type: command
short-summary: Deletes specific Api Version Set.
examples:
  - name: Deletes specific Api Version Set.
    text: |-
        az apim api versionset delete --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId
"""

helps['apim api schema create'] = """
type: command
short-summary: Create an API Management API Schema.
parameters:
  - name: --api-id
    type: string
    short-summary: unique name of the api for which schema needs to be created
    long-summary: |
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
  - name: --schema-id
    type: string
    short-summary: unique name of the api schema to be created
    long-summary: |
        Schema identifier. Must be unique in the current API Management service instance.
  - name: --schema-path
    type: string
    short-summary: File path specified to import schema of the API.
    long-summary: |
        Specify either --schema-path or --schema-content not both
  - name: --schema-content
    type: string
    short-summary: Json escaped string defining the document representing the Schema
    long-summary: |
        Specify either --schema-path or --schema-content not both
  - name: --schema-type
    type: string
    short-summary: Schema type  (e.g. application/json, application/vnd.ms-azure-apim.graphql.schema).
    long-summary: |
        Must be a valid media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document
examples:
  - name: Create a API Schema.
    text: |-
        az apim api schema create --service-name MyApim -g MyResourceGroup --api-id MyApi --schema-id schemaId --schema-type schemaType --schema-path schemaFilePath
"""

helps['apim api schema delete'] = """
type: command
short-summary: Delete an API Management API Schema.
examples:
  - name: delete a API Schema.
    text: |-
            az apim api schema delete --service-name MyApim -g MyResourceGroup --api-id MyApi --schema-id schemaId
"""

helps['apim api schema show'] = """
type: command
short-summary: Show details of an API Management API Schema.
examples:
  - name: Get a API Schema.
    text: |-
            az apim api schema show --service-name MyApim -g MyResourceGroup --api-id MyApi --schema-id schemaId
"""

helps['apim api schema list'] = """
type: command
short-summary: List API Management API schema's.
examples:
  - name: Get list of schema's associated with an api id.
    text: |-
            az apim api schema list --service-name MyApim -g MyResourceGroup --api-id MyApi
"""

helps['apim api schema get-etag'] = """
type: command
short-summary: Get etag of an API Management API schema.
examples:
  - name: get a schema entity tag.
    text: |-
            az apim api schema get-etag --service-name MyApim -g MyResourceGroup --api-id MyApi --schema-id schemaId
"""

helps['apim api schema wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of an apim api schema is met.
examples:
  - name: Place the CLI in a waiting state until a condition of a apim api schema is met.
    text: |
        az apim api schema wait --created --api-id MyApi --name MyApim --schema-id schemaId -g MyResourceGroup
    crafted: true
"""

helps['apim deletedservice show'] = """
type: command
short-summary: Get soft-deleted Api Management service instances available for undelete by name.
examples:
  - name: Get a soft-deleted services with its name.
    text: |
        az apim deletedservice show --service-name MyApim --location westus
"""

helps['apim deletedservice list'] = """
type: command
short-summary: List all soft-deleted Api Management services instances available for undelete for the given subscription.
examples:
  - name: List all soft-deleted services in a subscription.
    text: |
        az apim deletedservice list
"""

helps['apim deletedservice purge'] = """
type: command
short-summary: Purge soft-deleted Api Management service instance (deletes it with no option to undelete)
examples:
  - name: Purge a soft-deleted serivce.
    text: |
        az apim deletedservice purge --service-name MyApim --location westus
"""

helps['apim graphql resolver create'] = """
type: command
short-summary: Create a new resolver in the GraphQL API or updates an existing one.
examples:
  - name: Create a new resolver.
    text: |
        az apim api create --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId --display-name "Query-allFamilies" --path "Query/allFamilies" --description "A GraphQL Resolver example"
"""

helps['apim graphql resolver delete'] = """
type: command
short-summary: Delete the specified resolver in the GraphQL API.
examples:
  - name: Delete resolver.
    text: |
        az apim api delete --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId
"""

helps['apim graphql resolver show'] = """
type: command
short-summary: Get the details of the GraphQL API Resolver specified by its identifier.
examples:
  - name: Get details of resolver.
    text: |
        az apim api show --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId
"""

helps['apim graphql resolver list'] = """
type: command
short-summary: List a collection of the resolvers for the specified GraphQL API.
examples:
  - name: Get list of resolvers of an API.
    text: |
        az apim api show --service-name MyApim -g MyResourceGroup --api-id MyApi
"""

helps['apim graphql resolver policy create'] = """
type: command
short-summary: Create or updates policy configuration for the GraphQL API Resolver level.
examples:
  - name: Create a resolver policy.
    text: |
        az apim graphqlapi resolver policy create --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId --format xml --value-path 'path to xml file'
"""

helps['apim graphql resolver policy get'] = """
type: command
short-summary: Get the policy configuration at the GraphQL API Resolver level.
examples:
  - name: Get policy configuration.
    text: |
        az apim graphqlapi resolver policy show --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId
"""

helps['apim graphql resolver policy delete'] = """
type: command
short-summary: Delete the policy configuration at the GraphQL Api Resolver.
examples:
  - name: Delete policy configuration.
    text: |
        az apim graphqlapi resolver policy delete --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId
"""

helps['apim graphql resolver policy list'] = """
type: command
short-summary: Get the list of policy configuration at the GraphQL API Resolver level.
examples:
  - name: Get list of policy configuration.
    text: |
        az apim graphqlapi resolver list delete --service-name MyApim -g MyResourceGroup --api-id MyApi --resolver-id MyResolverId
"""
