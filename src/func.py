from pprint import pprint
import re
from utils import Utils
from permissions import PermissionHandler


class core:

    def __init__(self):
        pass

    def print(self):
        pass

    def pagination_str(self):
       
       endCursor = "5756765557"
       cycle_count = 0
       is_next_page = True
       pattern = r"\$after\s*:\s*after\s*"
    
       payload = """
           "query": "query GetFilesetSnapshots(
                        $filesetId: UUID!
                        $slaDomainId: UUID
                        $startDate: String
                        $endDate: String
                        $limit: Int = 10
                        $offset: Int = 0
                        $after: after
                        {
                        fileset(id: $filesetId) {
                          id
                          name
                          host {
                            id
                            name
                          }
                          slaDomain {
                            id
                            name
                          }
                          snapshots(
                            filter: {
                              slaDomainId: $slaDomainId
                              timeRange: { start: $startDate, end: $endDate }
                            }
                            first: $limit
                            offset: $offset
                          ) {
                            nodes {
                              id
                              date
                              status
                              retentionDuration
                            }
                            pageInfo {
                              hasNextPage
                              hasPreviousPage
                              totalCount
                              after
                            }
                          }
                        }     
                       " , 
           "variables":
                {
                  "filesetId": "123e4567-e89b-12d3-a456-426614174000",
                  "slaDomainId": "321e4567-e89b-12d3-a456-426614174000",
                  "startDate": "2025-01-01T00:00:00Z",
                  "endDate": "2025-01-18T23:59:59Z",
                  "after": endCursor,
                  "offset": 0
               }
           """
    
       while is_next_page and cycle_count != 3:
           if cycle_count == 0:
               payload = re.sub(pattern, "", payload)
               print(
                   f"Payload after removing `after` (cycle_count={cycle_count}):\n{payload}"
               )
               cycle_count += 1
           else:
               print(
                   f"Payload without modification (cycle_count={cycle_count}):\n{payload}"
               )
               cycle_count += 1


    def update_permissions_role(self):
        """
        Parcourt les rôles et affiche les permissions avec leurs IDs correspondants.
        """

        roles = Utils.load_yaml("/Users/lucas/Desktop/py/src/role.yaml")

        for role_name, role_data in roles.items():
            print(f"Role: {role_name}")
            
            permissions = role_data.get('permissions', {}).get('accept', [])
            print("Permissions:")
            
            for permission in permissions:
                object_id = PermissionHandler.return_object_id(permission)
                print(f"  - {permission}: {object_id}")