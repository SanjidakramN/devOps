try { 
    $check = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $Principal = New-Object Security.Principal.WindowsPrincipal ($check)
    $is_admin = $Principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
if ($is_admin) {
        Write-Output "you are admininistrator"
 } else {
        Write-Output "dont have admin rights."
     }
 } catch {
        Write-Output "Error: in line number $($_.InvocationInfo.ScriptLineNumber) : $($Error[0])"
    }